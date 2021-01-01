import sys
import requests
from decouple import config

GITHUB_USER = config("GITHUB_USER")
API_TOKEN = config("GITHUB_API_TOKEN")
BASE_URL = 'https://api.github.com/'


body = {}

args = sys.argv
for arg_i in range(len(args)):
    if args[arg_i] == "-n" or args[arg_i] == "--name":
        body['name'] = args[arg_i + 1]
    elif args[arg_i] == "-d" or args[arg_i] == "--description":
        body['description'] = args[arg_i + 1]


body['auto_init'] = True
body['license_template'] = 'mit'

url = BASE_URL + 'user/repos'
resp = requests.post(
    url,
    auth=(GITHUB_USER, API_TOKEN),
    json=body
)

print(resp.status_code)
