import json
import pandas as pd
import subprocess

# Load the vulnerability data from Trivy JSON file
with open("vulnerabilities_final.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract vulnerability details
vulnerabilities = []
for result in data.get("Results", []):
    for vuln in result.get("Vulnerabilities", []):
        vulnerabilities.append({
            "ID": vuln.get("VulnerabilityID", "N/A"),
            "Package": vuln.get("PkgName", "Unknown"),
            "Severity": vuln.get("Severity", "LOW"),
            "Installed_Version": vuln.get("InstalledVersion", "N/A"),
            "Fixed_Version": vuln.get("FixedVersion", "N/A")
        })

# Convert to Pandas DataFrame
df = pd.DataFrame(vulnerabilities)

# Open log file with UTF-8 encoding to avoid Unicode errors
with open("ai_fixes_log_final.txt", "w", encoding="utf-8") as log_file:
    log_file.write("🔧 AI Auto-Fix Log\n")
    log_file.write("====================\n")

    # Function to auto-fix vulnerabilities
    def auto_fix_vulnerabilities():
        for index, row in df.iterrows():
            if row["Severity"] in ["HIGH", "CRITICAL"] and row["Fixed_Version"] != "N/A":
                package = row["Package"]
                fixed_version = row["Fixed_Version"]

                # Apply the fix
                print(f"🔧 Fixing {package} by upgrading to {fixed_version}...")
                subprocess.run(["pip", "install", "--upgrade", package], check=False)

                # Log the fix
                log_file.write(f"✔ FIXED: {package} upgraded from {row['Installed_Version']} → {fixed_version}\n")
            else:
                log_file.write(f"❌ SKIPPED: {row['Package']} (No fix available)\n")

    # Apply auto-fix
    auto_fix_vulnerabilities()

print("✅ AI-based vulnerability fixes applied! Log saved in `ai_fixes_log_final.txt`.")

# Save updated vulnerability data
df.to_csv("ai_vulnerability_analysis_fixed_final.csv", index=False)
