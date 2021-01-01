#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export $(grep -v '^#' $DIR/.env | xargs)

REPO_NAME=$1
REPO_DESCRIPTION=$2

if [ -z $REPO_NAME ]; then
    printf $'\e[31mERROR:\e[0m you must supplay a repository name! '
    printf $'Run \e[33mcreate_project --help\e[0m to get more information.\n'
    exit 1
elif [ $REPO_NAME = "--help" ]; then
    printf $'\n\e[1mUsage : \e\n[0m'
    printf $'  \e[32mcreate_project \e[34mmy_new_project \e[33m"the project description."\e[0m\n\n'
    printf $'\e[1mOR \e[0m (if you don\'t want to add a description : \n'
    printf $'  \e[32mcreate_project \e[34mmy_new_project\e[0m\n\n'
    exit 0
fi


finalize () {
  git clone "https://github.com/$GITHUB_USER/$REPO_NAME.git"
  code ./$REPO_NAME
  exit 0
}


STATUS_CODE=$(python3 $DIR/create_project.py --name $REPO_NAME --description "${REPO_DESCRIPTION}")

case "$STATUS_CODE" in 
  "201" ) finalize;;
  "422" ) printf $'❌ repository \e[34m'"${REPO_NAME}"$'\e[0m already exists!\n' && exit 1;;
  * ) echo "❌  error: ${STATUS_CODE}" && exit 1;;
esac