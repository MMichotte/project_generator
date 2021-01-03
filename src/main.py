"""
@Author: Martin Michotte
"""
import sys
from helpers import parse_args, create_local_project, check_for_dir
from services import create_github_repo

if __name__ == "__main__":
    repo = parse_args()
    check_for_dir(repo)
    new_repo = create_github_repo(repo)
    create_local_project(new_repo)
    sys.exit(0)