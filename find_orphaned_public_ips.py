from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
import yaml

with open("../config/config.yaml") as f:
    config = yaml.safe_load(f)

subscription_id = config["subscription_id"]

credential = DefaultAzureCredential()
network_client = NetworkManagementClient(credential, subscription_id)

print("Orphaned Public IPs:")

for ip in network_client.public_ip_addresses.list_all():
    if not ip.ip_configuration:
        print(ip.name)
