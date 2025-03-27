import json
import pandas as pd
from tabulate import tabulate

# Load Trivy JSON output
file_path = "vulnerabilities.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)
except json.JSONDecodeError as e:
    print(f"❌ JSON Decode Error: {e}")
    exit()
except FileNotFoundError:
    print(f"❌ Error: {file_path} not found!")
    exit()

# Extract vulnerability details
vulns = []
for result in data.get("Results", []):
    for vuln in result.get("Vulnerabilities", []):
        vulns.append([
            vuln["PkgName"],  # Affected package
            vuln["VulnerabilityID"],  # CVE ID
            vuln["Severity"],  # Risk level
            vuln["InstalledVersion"],  # Installed version
            vuln.get("FixedVersion", "Not Fixed"),  # Fixed version (if available)
            vuln["PrimaryURL"]  # More info
        ])

# Convert to DataFrame
df = pd.DataFrame(vulns, columns=["Package", "CVE ID", "Severity", "Installed", "Fixed", "More Info"])

# Print in a properly formatted table for PowerShell
print(tabulate(df, headers="keys", tablefmt="grid"))
