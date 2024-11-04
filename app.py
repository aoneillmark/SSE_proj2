from flask import Flask, render_template, request
import requests

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


@app.route("/receive_username", methods=["POST"])
def receive_username():
    username = request.form.get("username")

    # Provided code
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    if response.status_code == 200:
        repos = response.json()  
        # data returned is a list of ‘repository’ entities
        for repo in repos:
            print(repo["full_name"])
    # End provided code

    # Get commit
    # /repos/{owner}/{repo}/commits/{ref}
    # /response
    response2 = requests.get(f"https://api.github.com/repos/{username}/{repo}/commits")

    return render_template("hello_username.html",
                           username=username,
                           github_repos=response.json(),)
                        #    commits=response2.json())


# def process_query(animal):
#     if animal == "dinosaurs":
#         return "Dinosaurs ruled the Earth 200 million years ago"
#     else:
#         return "Unknown"
