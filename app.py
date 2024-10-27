from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_email = request.form.get("email")
    input_message = request.form.get("message")
    return render_template("hello.html",
                           email=input_email, message=input_message)
