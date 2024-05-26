from github import Github
from github import Auth
from dotenv import load_dotenv
import os

load_dotenv()

auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

g = Github(auth=auth)

def get_repos():
    repos = g.get_user().get_repos()
    return repos