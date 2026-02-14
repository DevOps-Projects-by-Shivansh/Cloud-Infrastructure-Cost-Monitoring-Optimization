import datetime
import yaml
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.monitor import MonitorManagementClient

with open("../config/config.yaml") as f:
    config = yaml.safe_load(f)

subscription_id = config["subscription_id"]
cpu_threshold = config["cpu_threshold"]

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)
monitor_client = MonitorManagementClient(credential, subscription_id)

idle_vms = []

for vm in compute_client.virtual_machines.list_all():
    vm_name = vm.name
    resource_group = vm.id.split("/")[4]

    metrics = monitor_client.metrics.list(
        vm.id,
        timespan=f"{datetime.datetime.utcnow() - datetime.timedelta(days=7)}/{datetime.datetime.utcnow()}",
        interval='PT1H',
        metricnames='Percentage CPU',
        aggregation='Average'
    )

    for item in metrics.value:
        for timeseries in item.timeseries:
            for data in timeseries.data:
                if data.average and data.average < cpu_threshold:
                    idle_vms.append(vm_name)

print("Idle VMs:")
for vm in set(idle_vms):
    print(vm)
