import streamlit as st
import boto3
import json
import anthropic
from datetime import datetime, timedelta

st.set_page_config(page_title="AWS Security Cost Dashboard", layout="wide")
st.title("AWS Security Cost Dashboard")
st.caption("Powered by AWS Security Hub, Cost Explorer, and Claude AI")

# ── Data fetchers ──────────────────────────────────────────────────────────────

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
        findings = []
        for f in response.get("Findings", []):
            findings.append({
                "title": f.get("Title"),
                "severity": f.get("Severity", {}).get("Label"),
                "resource": f.get("Resources", [{}])[0].get("Id", "unknown"),
                "description": f.get("Description")
            })
        return findings
    except Exception as e:
        return []

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
        return []

def get_ai_insight(findings, costs):
    client = anthropic.Anthropic()
    findings_text = json.dumps(findings, indent=2)
    costs_text = json.dumps(costs, indent=2)
    prompt = f"""You are a cloud security analyst. Analyze these AWS Security Hub findings and cost data and give a concise 3-5 sentence summary covering:
1. The most critical security risks and what they mean in plain English
2. Any cost concerns or observations
3. Your top 2 recommended actions

Security Hub Findings:
{findings_text}

Cost Data (last 30 days):
{costs_text}

Be direct and practical. Write for a security engineer, not an executive."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

# ── Layout ─────────────────────────────────────────────────────────────────────

col1, col2 = st.columns(2)

with st.spinner("Fetching live AWS data..."):
    findings = get_security_hub_findings()
    costs = get_cost_last_30_days()

# Metrics row
total = len(findings)
critical = len([f for f in findings if f["severity"] == "CRITICAL"])
high = len([f for f in findings if f["severity"] == "HIGH"])
low = len([f for f in findings if f["severity"] == "LOW"])

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Findings", total)
m2.metric("Critical", critical, delta=f"{critical} need immediate action" if critical > 0 else None, delta_color="inverse")
m3.metric("High", high)
m4.metric("Low", low)

st.divider()

# Security findings table
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader(" Security Hub Findings")
    if findings:
        for f in findings:
            severity = f["severity"]
            color = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵"}.get(severity, "⚪")
            with st.expander(f"{color} [{severity}] {f['title']}"):
                st.write(f"**Resource:** `{f['resource']}`")
                st.write(f"**Description:** {f['description']}")
    else:
        st.success("No active findings!")

with col2:
    st.subheader("Cost Last 30 Days")
    if costs:
        for c in costs:
            st.write(f"**{c['service']}**: ${c['cost_usd']}")
    else:
        st.info("No cost data yet — Cost Explorer may still be initializing.")

st.divider()

# AI Insights
st.subheader("Claude AI Security Insights")
if st.button("Generate AI Insights"):
    with st.spinner("Claude is analyzing your AWS environment..."):
        insight = get_ai_insight(findings, costs)
        st.info(insight)
