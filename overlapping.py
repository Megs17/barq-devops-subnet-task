import ipaddress
from itertools import combinations

# List of CIDR blocks of all subnets to check for overlaps
cidr_blocks = [
    "192.168.1.0/24", "10.1.4.0/23", "172.16.20.0/24", "192.168.100.0/22", "10.0.3.0/24",
    "172.16.0.0/23", "10.2.0.0/22", "192.168.2.0/24", "172.16.48.0/22", "10.10.0.0/23",
    "192.168.3.0/24", "10.20.4.0/22", "172.16.8.0/23", "10.4.3.0/24", "192.168.20.0/22",
    "172.16.40.0/24", "10.0.0.0/23", "192.168.10.0/24", "172.16.14.0/23", "10.3.0.0/22",
    "192.168.4.0/24", "10.50.2.0/24", "172.16.60.0/22", "192.168.6.0/23", "10.15.4.0/22"
]

# Convert strings of CIDR blocks to ip_network objects
networks = [ipaddress.ip_network(cidr) for cidr in cidr_blocks]

overlaps = []

# Check for overlaps between all pairs of networks
for net1, net2 in combinations(networks, 2):
    if net1.overlaps(net2):
        overlaps.append((str(net1), str(net2)))


if overlaps:
    print("Overlapping Subnets Found:")
    for net1, net2 in overlaps:
        print(f"- {net1} overlaps with {net2}")
else:
    print("No overlapping subnets found.")
