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


# @app.route("/query")
# def get_query():
#     query = request.args.get('q')
#     return process_query(query)


@app.route("/github")
def github():
    return render_template("new_API_page.html")


@app.route("/receive_username")
def receive_username():
    username = request.form.get("username")
    return render_template("hello_username.html",
                           username=username)


# def process_query(animal):
#     if animal == "dinosaurs":
#         return "Dinosaurs ruled the Earth 200 million years ago"
#     else:
#         return "Unknown"
