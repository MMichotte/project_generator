"""
@Author: Martin Michotte
"""
import sys
from colors import colors as c
import requests
from decouple import config


GITHUB_USER = config("GITHUB_USER")
API_TOKEN = config("GITHUB_API_TOKEN")
BASE_URL = 'https://api.github.com/'


def create_github_repo(repo):
    """
    docstring
    """
    yn = input(f'Create new repository with name : {c.green}{repo.name}{c.rst} ? (y/n)')
    if yn != "" and yn != "y" and yn !="Y":
        exit(0)
    
    url = BASE_URL + 'user/repos'
    resp = requests.post(
        url,
        auth=(GITHUB_USER, API_TOKEN),
        json=repo.get_json()
    )

    if resp.status_code == 201 :
        print("✅ Github Repository created")
        return {
            'GITHUB_USER':GITHUB_USER,
            'REPO': repo.name
        }
    elif resp.status_code == 401 :
        print(f'❌ Invalid credentials : ({resp.status_code}) : {resp.json()["message"]}')
        sys.exit(1)
    elif resp.status_code == 422 :
        print(f'❌ Repository {c.blue}{repo.name}{c.rst} already exists!')
        print(resp.json())
        sys.exit(1)
    else:
        print(f'❌ Unknown error: ({resp.status_code}) : {resp.json()}')
        sys.exit(1)

def get_available_licenses ():
    url = BASE_URL + 'licenses'
    resp = requests.get(url)
    
    licenses = []
    for lic in resp.json():
        licenses.append(lic["key"])
    
    return licenses

def get_available_gitignores ():
    url = BASE_URL + 'gitignore/templates'
    resp = requests.get(url)
    
    return resp.json()


if __name__ == "__main__":
    print(get_available_licenses())
    print(get_available_gitignores())
