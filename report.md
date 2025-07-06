# Subnet Analysis Report

---

## ❓ Q1: Which subnet has the most hosts?

Subnets with the most hosts are all those with a **/22 prefix** — each provides **1022 usable hosts**:

- 192.168.100.0/22  
- 192.168.20.0/22  
- 10.2.0.0/22  
- 10.3.0.0/22  
- 10.15.4.0/22  
- 10.20.4.0/22  
- 172.16.48.0/22  
- 172.16.60.0/22  

---

## ❓ Q2: Are there any overlapping subnets?

 **No subnet overlapping found.**

---

## ❓ Q3: What is the smallest and largest subnet in terms of address space?

### Smallest subnet(s):

All **/24** subnets → 256 total addresses

Examples:
- 192.168.1.0/24  
- 172.16.20.0/24  
- 10.0.3.0/24  
- 192.168.2.0/24  
- 192.168.3.0/24  
- 10.4.3.0/24  
- 172.16.40.0/24  
- 192.168.10.0/24  
- 192.168.4.0/24  
- 10.50.2.0/24  

---

### Largest subnet(s):

All **/22** subnets → 1024 total addresses

Examples:
- 192.168.100.0/22  
- 192.168.20.0/22  
- 10.2.0.0/22  
- 10.3.0.0/22  
- 10.15.4.0/22  
- 10.20.4.0/22  
- 172.16.48.0/22  
- 172.16.60.0/22  

---

## ❓ Q4: Suggest a subnetting strategy that could reduce wasted IPs in this network

### 🔎 Problem:

Large subnets have high usable IP counts, but most of them use only **1 IP**  
(as shown in `network_plot.png`), which leads to wasted space.

### 💡 Suggested Solution:

- Use **VLSM (Variable Length Subnet Masking)** to assign subnet sizes based on real usage.



