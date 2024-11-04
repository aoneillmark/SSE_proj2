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
for repo in repos:
    response2 = requests.get(f"https://api.github.com/repos/{username}/{repo["name"]}/commits")
    print(response2.json())
