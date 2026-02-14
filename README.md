# Azure Cloud Infrastructure Cost Monitoring & Optimization

## Overview
This project demonstrates cloud cost governance, anomaly detection, and automated resource optimization using Azure-native tools.

## Key Objectives
- Detect idle resources
- Prevent budget overruns
- Maintain governance & audit compliance
- Automate cost reporting
- Enable proactive financial monitoring

## Architecture
Azure Resources
   ├── Azure Monitor → Metric collection
   ├── Azure Cost Management → Budget tracking
   ├── Action Groups → Alert notifications
   ├── Python Scripts → Idle detection
   ├── Bash + Azure CLI → Controlled cleanup
   └── Grafana → Cost visualization

## Optimization Logic
- VM idle detection (CPU <5% for 7 days)
- Disk orphan detection
- Snapshot age validation (>30 days)
- Budget alert at 80% usage
