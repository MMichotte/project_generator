"""
@Author: Martin Michotte
"""
import os
import sys
from colors import colors as c
from Repository import Repository

SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_ROOT_DIR_PATH = '/'.join(os.path.realpath(__file__).split('/')[0:-2])

def parse_args ():
    """
    docstring
    """
    proj_name = None
    proj_description = ""
    proj_license = "mit"
    proj_git_ignore = None
    proj_is_private = False
    proj_with_readme = True

    args = enumerate(sys.argv[1:])
    for i, arg in args:
        if arg == "-h" or arg == "--help":
            f = open(f'{SCRIPT_ROOT_DIR_PATH}/man.txt', "rt", encoding='unicode_escape')
            print(f.read())
            f.close()
            sys.exit(0)

        elif arg == "-c" or arg == "--config":
            configure()
            sys.exit(0)

        elif arg == "-d" or arg == "--description":
            proj_description = next(args)[1]

        elif arg == "-nr" or arg == "--no_readme":
            proj_with_readme = False

        elif arg == "-l" or arg == "--license":
            proj_license = next(args)[1]
        
        elif arg == "-gi" or arg == "--git_ignore":
            proj_git_ignore = next(args)[1]

        elif arg == "-p" or arg == "--private":
            proj_is_private = True

        else:
            proj_name = arg

    if proj_name is None:
        print(f'{c.red}ERROR:{c.rst} you must supply a repository name! ')
        print(f'Run {c.green}create_project --help{c.rst} to get more information.\n')
        sys.exit(1)

    return Repository(proj_name, proj_description, proj_with_readme, proj_license, proj_git_ignore, proj_is_private)

def check_for_dotenv ():
    if not os.path.exists(f'{SCRIPT_ROOT_DIR_PATH}/.env'):
        print(f'{c.bold}Initial configuration (once) :{c.rst}')
        configure()

def configure ():
    """
    docstring
    """
    username = input(f'Enter your {c.bold}GitHub Username{c.rst} : ')
    token = input(f'Paste your {c.bold}GitHub Personal Access Token{c.rst} : ')
    f = open(f'{SCRIPT_ROOT_DIR_PATH}/.env', 'w')
    f.write(f'GITHUB_USER=\"{username}\"\nGITHUB_API_TOKEN=\"{token}\"')
    f.close()
    print(f'{c.green}Config saved{c.rst}\n')


def check_for_dir(repo):
    """
    docstring
    """
    if os.path.exists(f'./{repo.name}'):
        print(f'{c.red}ERROR:{c.rst} A project named {c.blue}{repo.name}{c.rst} already exists in this folder!')
        sys.exit(1)

def create_local_project (new_repo):
    """
    docstring
    """
    os.system(f'git clone \"https://github.com/{new_repo["GITHUB_USER"]}/{new_repo["REPO"]}.git\"')
    os.system(f'code ./{new_repo["REPO"]}')
    print('✅ Cloned remote locally!')

if __name__ == "__main__":
    print(SCRIPT_PATH)
    print(SCRIPT_ROOT_DIR_PATH)
    parse_args()
