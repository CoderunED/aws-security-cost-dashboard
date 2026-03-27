import boto3
import json

def get_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = [b["Name"] for b in response.get("Buckets", [])]
    return buckets

def get_ec2_regions():
    ec2 = boto3.client("ec2", region_name="us-east-1")
    response = ec2.describe_regions(Filters=[{"Name": "opt-in-status", "Values": ["opt-in-not-required"]}])
    regions = [r["RegionName"] for r in response["Regions"]]
    return regions

if __name__ == "__main__":
    print("=== S3 Buckets ===")
    buckets = get_s3_buckets()
    print(json.dumps(buckets, indent=2))

    print("\n=== EC2 Regions ===")
    regions = get_ec2_regions()
    print(json.dumps(regions, indent=2))
