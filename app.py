from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# USERS DATABASE
users = {
    "admin": {"password": "123", "role": "ADMIN"},
    "ravi": {"password": "123", "role": "HR"},
    "kiran": {"password": "123", "role": "DEV"}
}

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        password = request.form["password"].strip()

        if username in users and users[username]["password"] == password:
            session["user"] = username
            session["role"] = users[username]["role"]
            return redirect("/dashboard")

        return "Invalid Login"

    return render_template("login.html")


# ---------------- DASHBOARD ROUTER ----------------
@app.route("/dashboard")
def dashboard():
    role = session.get("role")

    if not role:
        return redirect("/")

    if role == "ADMIN":
        return redirect("/admin")
    elif role == "HR":
        return redirect("/hr")
    elif role == "DEV":
        return redirect("/dev")


# ---------------- ADMIN ----------------
@app.route("/admin")
def admin():
    if session.get("role") != "ADMIN":
        return "Access Denied"

    return render_template("admin.html", user=session["user"])


# ---------------- HR ----------------
@app.route("/hr")
def hr():
    if session.get("role") != "HR":
        return "Access Denied"

    return render_template("hr.html", user=session["user"])


# ---------------- DEV ----------------
@app.route("/dev")
def dev():
    if session.get("role") != "DEV":
        return "Access Denied"

    return render_template("dev.html", user=session["user"])


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    print("SERVER STARTING...")
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)