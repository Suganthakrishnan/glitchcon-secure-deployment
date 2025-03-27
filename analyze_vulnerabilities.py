import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the Trivy JSON output
with open("vulnerabilities.json", "rb") as file:
    raw_data = file.read().decode("utf-8", errors="ignore")  # Ignore problematic bytes
    data = json.loads(raw_data)  # Load JSON data


# Extract vulnerability details
vuln_list = []
for result in data.get("Results", []):
    for vuln in result.get("Vulnerabilities", []):
        vuln_list.append({
            "ID": vuln.get("VulnerabilityID", "Unknown"),
            "Package": vuln.get("PkgName", "Unknown"),
            "Severity": vuln.get("Severity", "Unknown"),
            "Description": vuln.get("Description", "No description available"),
        })

# Convert to DataFrame
df = pd.DataFrame(vuln_list)

# Convert severity to numerical values for AI analysis
severity_mapping = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1, "UNKNOWN": 0}
df["Severity_Score"] = df["Severity"].map(severity_mapping)

# AI-based Risk Scoring (Simple Risk Weighting)
df["Risk_Score"] = df["Severity_Score"] * 10  # Example: Multiply severity by 10

# Save processed data
df.to_csv("analyzed_vulnerabilities.csv", index=False)
df.to_json("analyzed_vulnerabilities.json", orient="records", indent=4)

# Display top 5 vulnerabilities
print("Top vulnerabilities based on risk score:")
print(df.sort_values(by="Risk_Score", ascending=False).head())
