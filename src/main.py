"""
@Author: Martin Michotte
"""
import sys
import subprocess
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
import helpers as h
import services as s


if __name__ == "__main__":
    repo = h.parse_args()
    h.check_for_dir(repo)
    new_repo = s.create_github_repo(repo)
    h.create_local_project(new_repo)
    sys.exit(0)