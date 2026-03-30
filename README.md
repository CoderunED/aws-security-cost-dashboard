# 🔐 AWS Security Cost Dashboard

An AI-powered dashboard that connects to a live AWS account, pulls real security and cost data, and uses Claude AI to generate plain-English analysis and recommendations.

![Dashboard Screenshot](screenshots/dashboard.png)

## 🚀 What It Does

- Pulls **live security findings** from AWS Security Hub
- Monitors **AWS spend** via Cost Explorer
- Uses **Claude AI** to analyze findings and surface the most critical risks
- Runs **automatically every Monday** via GitHub Actions

## 📊 Real Metrics

- **16 active security findings** detected across 1 AWS account
- **1 critical misconfiguration** identified (AWS Config disabled)
- **15 monitoring gaps** found across IAM, VPC, CloudTrail, and S3
- **2 AWS services** monitored for cost anomalies
- **Claude AI** generates plain-English insights on demand

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| AWS Security Hub | Security findings |
| AWS Cost Explorer | Billing data |
| Boto3 | AWS Python SDK |
| Claude API | AI analysis layer |
| Streamlit | Dashboard UI |
| GitHub Actions | Automated weekly scans |

## ⚙️ Setup

1. Clone the repo
2. Install dependencies
```bash
pip install boto3 anthropic streamlit
```
3. Configure AWS credentials
```bash
aws configure
```
4. Set your Anthropic API key
```bash
export ANTHROPIC_API_KEY=your_key_here
```
5. Run the dashboard
```bash
streamlit run dashboard/app.py
```

## 🔄 Automated Scanning

GitHub Actions runs a full security scan every Monday at 9am UTC. Results are logged directly in the Actions tab.

## 📝 Resume Bullets

- Detected 16 active security misconfigurations across a live AWS account, including 1 critical finding, by building an AI-powered dashboard integrating AWS Security Hub, Cost Explorer, and Claude AI for automated analysis.
- Reduced cloud security triage time by generating instant plain-English risk summaries using Claude AI, replacing manual review of raw AWS Security Hub JSON findings.
- Automated weekly AWS security posture monitoring across IAM, VPC, CloudTrail, and S3 by deploying GitHub Actions to run scheduled scans with zero manual intervention.
