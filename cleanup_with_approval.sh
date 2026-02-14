#!/bin/bash

echo "WARNING: This script will delete identified unused resources."
read -p "Type APPROVE to continue: " approval

if [ "$approval" != "APPROVE" ]; then
    echo "Cleanup aborted."
    exit 1
fi

echo "Deleting unattached disks..."
az disk list --query "[?diskState=='Unattached'].name" -o tsv | while read disk; do
    az disk delete --name $disk --yes
done

echo "Cleanup completed."
