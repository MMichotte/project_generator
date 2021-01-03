"""
@Author: Martin Michotte
"""
import os
import sys
from decouple import config
from colors import colors as c
from Repository import Repository

def configure ():
    """
    docstring
    """
    username = input(f'Enter your {c.bold}GitHub Username{c.rst} : ')
    token = input(f'Paste your {c.bold}GitHub Personal Access Token{c.rst} : ')
    f = open(f'{SCRIPT_ROOT_DIR_PATH}/.env', 'w')
    f.write(f'GITHUB_USER=\"{username}\"\nGITHUB_API_TOKEN=\"{token}\"\nLICENSE=None\nGITIGNORE=None')
    f.close()
    print(f'{c.green}Config saved{c.rst}\n')

SCRIPT_ROOT_DIR_PATH = '/'.join(os.path.realpath(__file__).split('/')[0:-2])
if not os.path.exists(f'{SCRIPT_ROOT_DIR_PATH}/.env'):
    print(f'{c.bold}Initial configuration (once) :{c.rst}')
    configure()
        
import services as s


def parse_args ():
    """
    docstring
    """
    proj_name = None
    proj_description = ""
    proj_license = config("LICENSE") if config("LICENSE") != 'None' else None
    proj_git_ignore = config("GITIGNORE") if config("GITIGNORE") != 'None' else None
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
        
        elif arg == "--config-defaults":
            configure_defaults()
            sys.exit(0)

        elif arg == "-d" or arg == "--description":
            proj_description = next(args)[1]

        elif arg == "-nr" or arg == "--no-readme":
            proj_with_readme = False

        elif arg == "-l" or arg == "--license":
            proj_license = next(args)[1]
        
        elif arg == "-gi" or arg == "--gitignore":
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

def configure ():
    """
    docstring
    """
    username = input(f'Enter your {c.bold}GitHub Username{c.rst} : ')
    token = input(f'Paste your {c.bold}GitHub Personal Access Token{c.rst} : ')
    f = open(f'{SCRIPT_ROOT_DIR_PATH}/.env', 'w')
    f.write(f'GITHUB_USER=\"{username}\"\nGITHUB_API_TOKEN=\"{token}\"\nLICENSE=None\nGITIGNORE=None')
    f.close()
    print(f'{c.green}Config saved{c.rst}\n')

def configure_defaults ():
    """
    docstring
    """
    yn = input(f'Do you want to add a default license ? (y/n) ')
    if yn == "" or yn == "y" or yn =="Y":
        lic = input(f'Enter your default license : ')
        available_lics = s.get_available_licenses()
        flag=False
        while True:
            for l in available_lics:
                if l == lic or lic == 'None':
                    flag = True
                    f = open(f'{SCRIPT_ROOT_DIR_PATH}/.env', 'r')
                    lines = f.readlines()
                    f.close()
                    f = open(f'{SCRIPT_ROOT_DIR_PATH}/.env', 'w')
                    f.write(f'{lines[0]}{lines[1]}LICENSE={lic}\n{lines[3]}')
                    f.close()
                    break
            if flag:
                break
            print(f'{c.yellow}Invalid license.{c.rst} You can choose between : {available_lics}\nOr type < None > to remove the current default\n')
            lic = input(f'Enter your default license : ')
            

    yn = input(f'Do you want to add a default .gitignore ? (y/n) ')
    if yn == "" or yn == "y" or yn =="Y":
        ign = input(f'Enter your default .gitignore template : ')
        available_igns = s.get_available_gitignores()
        flag=False
        while True:
            for l in available_igns:
                if l == ign or ign == 'None':
                    flag = True
                    f = open(f'{SCRIPT_ROOT_DIR_PATH}/.env', 'r')
                    lines = f.readlines()
                    f.close()
                    f = open(f'{SCRIPT_ROOT_DIR_PATH}/.env', 'w')
                    f.write(f'{lines[0]}{lines[1]}{lines[2]}GITIGNORE={ign}')
                    f.close()
                    break
            if flag:
                break
            print(f'{c.yellow}Invalid .gitignore .{c.rst} You can choose between : {available_igns}\nOr type < None > to remove the current default.\n')
            ign = input(f'Enter your default .gitignore template : ')

    exit(0)

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
    print(SCRIPT_ROOT_DIR_PATH)
    parse_args()
