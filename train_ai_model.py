print("Script is running...")  # Debugging print

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("Loading dataset...")
df = pd.read_csv("analyzed_vulnerabilities.csv")

print("Dataset loaded successfully!")
print(df.head())  # Show first few rows

# Encode severity levels
severity_mapping = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1, "UNKNOWN": 0}
df["Severity_Score"] = df["Severity"].map(severity_mapping)

# Add random labels for exploitability (since we don’t have real labels)
df["Exploitable"] = np.random.choice([0, 1], size=len(df))  

# Features and target variable
X = df[["Severity_Score", "Risk_Score"]]
y = df["Exploitable"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression Model
print("Training AI model...")
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Plot results
plt.scatter(X_test["Severity_Score"], X_test["Risk_Score"], c=y_pred, cmap="coolwarm")
plt.xlabel("Severity Score")
plt.ylabel("Risk Score")
plt.title("Vulnerability Exploitability Prediction")
plt.show()
