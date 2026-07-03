from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = sqlite3.connect("boutique.db")

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        connection.close()

        if user:

            return redirect(url_for("dashboard"))

        else:

            return render_template(
                "login.html",
                error="Invalid Username or Password!"
            )

    return render_template("login.html")

# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Customers Page
@app.route("/customers")
def customers():
    return render_template("customers.html")

if __name__ == "__main__":
    app.run(debug=True)