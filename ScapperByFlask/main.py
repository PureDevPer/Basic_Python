from flask import Flask, render_template

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<username>")
def contact(username):
    return f"Hello! I am {username}"


app.run(host="0.0.0.0")
