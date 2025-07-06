import json
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def no_decimals(y, _):
    return f"{int(y)}"

# Load JSON data
with open("subnet_report.json", "r") as f:
    data = json.load(f)

# Prepare data for plotting
subnet_labels = []
used_counts = []
reserved_counts = []

for cidr, records in data.items():
    used = len(records)
    usable_hosts = records[0]["Usable Hosts"]
    reserved = usable_hosts - used
    subnet_labels.append(cidr)
    used_counts.append(used)
    reserved_counts.append(reserved)

## Sort the data by subnet labels
sorted_data = sorted(zip(subnet_labels, used_counts, reserved_counts), key=lambda x: x[0])
subnet_labels, used_counts, reserved_counts = zip(*sorted_data)


# Create one figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True)

# Plot Used Hosts
ax1.bar(subnet_labels, used_counts, color='skyblue')
ax1.set_title("Used Hosts per Subnet")
ax1.set_ylabel("Used Hosts")
ax1.grid(axis='y')
ax1.yaxis.set_major_formatter(FuncFormatter(no_decimals))

# Plot Reserved Hosts
ax2.bar(subnet_labels, reserved_counts, color='salmon')
ax2.set_title("Unused Hosts per Subnet")
ax2.set_ylabel("Unused Hosts")
ax2.set_xlabel("CIDR Notation (Subnet)")
ax2.grid(axis='y')
for i, v in enumerate(reserved_counts):
    ax2.text(i, v + 10, str(v), ha='center', fontsize=9)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout and save png image
plt.tight_layout()
plt.savefig("network_plot.png")
