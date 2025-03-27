from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def run_trivy_scan(file_path):
    """
    Dummy function to simulate running Trivy.
    Replace this with your actual scanning logic if desired.
    """
    dummy_scan = {
        "Results": [
            {
                "Vulnerabilities": [
                    {
                        "VulnerabilityID": "CVE-2024-1234",
                        "Severity": "High",
                        "Description": "Remote Code Execution vulnerability"
                    },
                    {
                        "VulnerabilityID": "CVE-2023-5678",
                        "Severity": "Medium",
                        "Description": "Privilege Escalation vulnerability"
                    }
                ]
            }
        ]
    }
    return dummy_scan.get("Results", [])

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Simulate Trivy scan
    vulnerabilities = run_trivy_scan(file_path)

    response = {
        "file": file.filename,
        "status": "Scan Complete",
        "vulnerabilities": vulnerabilities
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
