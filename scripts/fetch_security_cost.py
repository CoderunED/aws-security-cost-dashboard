import boto3
import json
from datetime import datetime, timedelta

def get_security_hub_findings():
    client = boto3.client("securityhub", region_name="us-east-1")
    try:
        response = client.get_findings(
            Filters={
                "RecordState": [{"Value": "ACTIVE", "Comparison": "EQUALS"}],
                "WorkflowStatus": [{"Value": "NEW", "Comparison": "EQUALS"}]
            },
            MaxResults=20
        )
        findings = response.get("Findings", [])
        summary = []
        for f in findings:
            summary.append({
                "title": f.get("Title"),
                "severity": f.get("Severity", {}).get("Label"),
                "resource": f.get("Resources", [{}])[0].get("Id", "unknown"),
                "description": f.get("Description")
            })
        return summary
    except Exception as e:
        return {"error": str(e)}

def get_cost_last_30_days():
    client = boto3.client("ce", region_name="us-east-1")
    try:
        end = datetime.today().strftime("%Y-%m-%d")
        start = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d")
        response = client.get_cost_and_usage(
            TimePeriod={"Start": start, "End": end},
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
            GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}]
        )
        results = []
        for period in response["ResultsByTime"]:
            for group in period["Groups"]:
                service = group["Keys"][0]
                cost = float(group["Metrics"]["UnblendedCost"]["Amount"])
                if cost > 0:
                    results.append({"service": service, "cost_usd": round(cost, 4)})
        results.sort(key=lambda x: x["cost_usd"], reverse=True)
        return results
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("=== Security Hub Findings ===")
    findings = get_security_hub_findings()
    print(json.dumps(findings, indent=2))

    print("\n=== AWS Cost Last 30 Days ===")
    costs = get_cost_last_30_days()
    print(json.dumps(costs, indent=2))
