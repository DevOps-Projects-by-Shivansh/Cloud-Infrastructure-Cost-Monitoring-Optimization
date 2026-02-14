import pandas as pd
from datetime import datetime

data = {
    "Resource Type": ["VM", "Disk", "Public IP"],
    "Unused Count": [3, 2, 1],
    "Estimated Monthly Cost Saved ($)": [150, 40, 10]
}

df = pd.DataFrame(data)
filename = f"weekly_cost_report_{datetime.now().date()}.csv"
df.to_csv(filename, index=False)

print(f"Cost report generated: {filename}")
