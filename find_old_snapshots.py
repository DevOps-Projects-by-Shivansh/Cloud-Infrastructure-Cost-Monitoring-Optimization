import datetime
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import yaml

with open("../config/config.yaml") as f:
    config = yaml.safe_load(f)

subscription_id = config["subscription_id"]
retention_days = config["snapshot_retention_days"]

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

print("Old Snapshots (>30 days):")

for snapshot in compute_client.snapshots.list():
    age = (datetime.datetime.utcnow() - snapshot.time_created.replace(tzinfo=None)).days
    if age > retention_days:
        print(snapshot.name)
