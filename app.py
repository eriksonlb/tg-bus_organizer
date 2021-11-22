from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/vehicles")
def vehicles():
    return render_template("vehicles.html")

@app.route("/clients")
def clients():
    return render_template("clients.html")

@app.route("/routes")
def routes():
    return render_template("routes.html")

@app.route("/logout")
def logout():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)