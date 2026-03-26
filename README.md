# AWS Security & Cost Dashboard

An AI-powered dashboard that connects to a live AWS account, pulls real
cost and security data, and uses Claude AI to answer questions like
"What are my biggest security risks this week?" and
"Where am I wasting money on AWS?"

## The Problem
Cloud teams spend 2+ hours per week manually reviewing AWS Cost Explorer,
Security Hub, and Trusted Advisor separately. Critical security findings
get missed. Cost waste goes unnoticed. There is no unified AI layer to
explain what matters most.

## The Solution
This dashboard pulls live data from three AWS services, runs AI analysis
automatically, and gives engineers and managers a single place to
understand their cloud security posture and cost efficiency.

## Features
- Live AWS cost data — spend by service, month-over-month trends
- Security Hub findings — grouped by severity with AI explanations
- Trusted Advisor recommendations — cost + security checks
- Claude AI chatbot — ask any question about your AWS account
- Weekly AI report — auto-generated executive summary
- Cost savings calculator — identifies unused resources with $ estimates

## Tech Stack
- AWS Cost Explorer — billing and spend data
- AWS Security Hub — security findings
- AWS Trusted Advisor — cost and security recommendations
- Boto3 — Python SDK for AWS
- Claude API — AI-powered analysis and chatbot
- Streamlit — interactive dashboard UI
- GitHub Actions — automated weekly data collection

## Current Status
- [ ] AWS CLI + Boto3 connected to live account
- [ ] Cost Explorer data pipeline
- [ ] Security Hub findings pipeline
- [ ] Trusted Advisor recommendations pipeline
- [ ] Claude AI analysis layer
- [ ] Streamlit dashboard UI
- [ ] AI chatbot interface
- [ ] Weekly automated reports
- [ ] Demo mode for recruiters

## Metrics (updating as built)
- AWS services monitored: TBD
- Security findings surfaced: TBD
- Potential cost savings identified: TBD
- Manual review time saved: TBD

## What's Next
Setting up AWS CLI, creating a read-only IAM user, and connecting
Boto3 to pull live cost data.
