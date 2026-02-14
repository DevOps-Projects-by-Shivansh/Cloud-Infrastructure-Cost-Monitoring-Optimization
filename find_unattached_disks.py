from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import yaml

with open("../config/config.yaml") as f:
    config = yaml.safe_load(f)

subscription_id = config["subscription_id"]

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

print("Unattached Disks:")

for disk in compute_client.disks.list():
    if disk.disk_state == "Unattached":
        print(disk.name)
