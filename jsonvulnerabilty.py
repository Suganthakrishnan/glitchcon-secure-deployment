import json

file_path = "vulnerabilities.json"

# Load JSON file
with open(file_path, "r") as file:
    data = json.load(file)

# Count vulnerabilities
vuln_count = sum(len(result.get("Vulnerabilities", [])) for result in data.get("Results", []))

print(f"✅ Total Vulnerabilities Found: {vuln_count}")
