from flask import Flask, request, redirect, url_for, session
import datetime

app = Flask(__name__)

failed_attempts = {}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    ip = request.remote_addr  # Get user's IP address

    # If user has failed 5 times, block them
    if failed_attempts.get(ip, 0) >= 5:
        log_attempt(ip, "BLOCKED")
        return "Too many failed attempts. You are blocked!", 403

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Hardcoded login (only "admin" works)
        if username == "admin" and password == "password123":
            failed_attempts[ip] = 0  # Reset failed attempts after success
            log_attempt(ip, "SUCCESS")
            return "Login Successful!"

        # Increase failed login count
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
        log_attempt(ip, f"FAILED Attempt {failed_attempts[ip]}/5")
        return f"Login Failed! Attempt {failed_attempts[ip]}/5"

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/profile")
def profile():
    return "Profile Page Works!"

# Function to log login attempts
def log_attempt(ip, status):
    with open("security_logs.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - IP: {ip} - Status: {status}\n")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
