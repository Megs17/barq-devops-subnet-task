# 📘 Subnet Visualizer

This tool processes an Excel file containing IP addresses and subnet masks. It calculates key network details such as CIDR notation, network address, broadcast address, and the number of usable hosts. It can also generate a bar chart visualization of the number of hosts in each subnet.

---

## 📂 Input Format

Ensure the input file (`ip_data.xlsx`) contains two columns with the following headers:

| IP Address      | Subnet Mask     |
|-----------------|-----------------|
| 192.168.1.24    | 255.255.255.0   |
| 10.1.5.4        | 255.255.254.0   |
| ...             | ...             |

---

##  How to Run

### ✅ Run Locally (with Python)

1. Install Python 3 and pip (if not installed).
2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the scripts:

```bash
python subnet_analyzer.py
python visualize.py
```

---

### 🐳 Run with Docker

Make sure Docker is installed, then follow these steps:

#### 1. Build the Docker image:

```bash
docker build -t subnet-visualizer .
```

#### 2. Run the container and you need to pass name of input file default ip_data.xlsx:

```bash
docker run --rm \
  -v "$PWD:/data" \
  -w /data \
  -e INPUT_FILE=ip_data.xlsx \
  subnet-visualizer
```
#### 3. Or you can run the published imaged without need to build:

```bash
docker run --rm \
  -v "$PWD:/data" \
  -w /data \
  -e INPUT_FILE=ip_data.xlsx \
  megs17/subnet-visualizer
```

This will run both `subnet_analyzer.py` and `visualize.py` inside the Docker container and mount your current directory for input and output.

---

## 📦 Output Files

- `subnet_report.json` — calculated network details.
- `network_plot.png` — bar chart of usable hosts per subnet.

---

## 🛠 Requirements

- Python 3.x
- pandas
- matplotlib
- openpyxl
- ipaddress (built-in in Python 3.3+)

All dependencies are listed in `requirements.txt`.


## 🙋‍♂️ Author

Developed by **Ahmed Magdy** — DevOps enthusiast with a passion for automation, cloud architecture, and networking.  
🔗 [GitHub](https://github.com/megs17) | 📧 ahmedfec2000@gmail.com | 🔗 [LinkedIn](https://www.linkedin.com/in/ahmed-magdy-178347233/)
