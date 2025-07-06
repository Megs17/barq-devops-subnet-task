import pandas as pd
import ipaddress
import json
from collections import defaultdict
import os

# Get input file name from environment variable or use default

input_file = os.getenv("INPUT_FILE", "ip_data.xlsx")  

# Convert subnet mask to prefix length (/24)

def subnetmask_to_prefix(subnet_mask):
    return ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}').prefixlen



# Calculate network details (CIDR, network address, broadcast, usable hosts)

def calculate_network_details(ip, subnet_mask):
    prefix = subnetmask_to_prefix(subnet_mask)
    network_data = ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False)
    network_address = str(network_data.network_address)
    cidr_notation = f"{network_address}/{prefix}"

    if network_data.num_addresses > 2:
        usable_hosts = network_data.num_addresses - 2
    else:
        usable_hosts = 0

    return cidr_notation, {
        "IP Address": ip,
        "Subnet Mask": subnet_mask,
        "CIDR Notation": cidr_notation,
        "Network Address": network_address,
        "Broadcast Address": str(network_data.broadcast_address),
        "Usable Hosts": usable_hosts
    }


# Read input Excel file

df = pd.read_excel(input_file)


# Dictionary to group results by CIDR notation

grouped_results = defaultdict(list)


# Dictionary to group results by CIDR notation

for index, row in df.iterrows():
    ip = row["IP Address"]
    subnet = row["Subnet Mask"]
    try:
        cidr, result = calculate_network_details(ip, subnet)
        grouped_results[cidr].append(result)
    except ValueError as e:
        print(f"Skipping invalid entry {ip}/{subnet}: {e}")


# Save grouped results to a JSON file

with open("subnet_report.json", "w") as json_file:
    json.dump(grouped_results, json_file, indent=4)

print("Network details saved to subnet_report.json")