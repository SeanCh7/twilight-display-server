from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/config")
def config():
    return render_template("config.html")


@app.route("/control")
def control():
    return render_template("control.html")


@app.route("/display/audience")
def display():
    return render_template("display_audience.html")


@app.route("/display/fta")
def display_admin():
    return render_template("display_fta.html")


def main():
    app.run(host="0.0.0.0", port=8080)


main()
