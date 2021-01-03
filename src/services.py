"""
@Author: Martin Michotte
"""
import sys
import subprocess
from helpers import check_for_dotenv
from colors import colors as c
try:
    import requests
    if not hasattr(requests, 'post'):
        raise ImportError
    from decouple import config
except ImportError:
    print(f'{c.yellow}WARNING:{c.rst} Some modules are missing, trying to install them :')
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'python-decouple'])
        print(f'{c.green}SUCCES:{c.rst} All required modules were successfully installed.')
        sys.exit(0)
    except Exception:
        print(f'{c.red}ERROR:{c.rst} Some modules couldn\'t be installed.')
        sys.exit(1)


check_for_dotenv()

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
        sys.exit(1)
    else:
        print(f'❌ Unknown error: ({resp.status_code}) : {resp.json()}')
        sys.exit(1)
