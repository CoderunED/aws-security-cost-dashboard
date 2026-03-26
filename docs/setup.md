# AWS Setup Guide

## Prerequisites
- AWS account
- AWS CLI installed (brew install awscli)
- IAM user with read-only permissions

## IAM Policies Required
- ReadOnlyAccess
- SecurityAudit
- AWSTrustedAdvisorReadOnlyAccess
- AWSSecurityHubReadOnlyAccess

## Configure AWS CLI
```bash
aws configure
```

## Verify Connection
```bash
aws sts get-caller-identity
```
