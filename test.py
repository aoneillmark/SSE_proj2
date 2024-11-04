from flask import Flask, render_template, request
import requests

username = "aoneillmark"
response = requests.get(f"https://api.github.com/users/{username}/repos")
if response.status_code == 200:
    repos = response.json() # data returned is a list of ‘repository’ entities
    for repo in repos:
        print(repo["full_name"])
else: 
    print("Problem here...")

repo_commits = []
for repo in repos:
    response2 = requests.get(f"https://api.github.com/repos/{username}/{repo["name"]}/commits")
    recent_commit = response2.json()[0] if response2.json() else None
    repo_commits.append({
        "repo": repo,
        "commit": recent_commit,
    })

