from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/experience/")
def experience():
    return render_template("experience.html")

@app.route("/portfolio/")
def profile():
    return render_template("portfolio.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)