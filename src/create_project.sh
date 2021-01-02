#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" # parent directory of this code 
CODE_DIR="$( cd $DIR && cd .. >/dev/null 2>&1 && pwd )"                 # directory of this code 

REPO_DESCRIPTION=""
REPO_LICENSE="mit"
CONFIGURE=false

main () {
  while [[ "$#" -gt 0 ]]; do
    case "$1" in
      -d|--description) REPO_DESCRIPTION="$2"; shift 2;;
      -l|--license) REPO_LICENSE="$2"; shift 2;;
      -c|--config) CONFIGURE=true; break ;;
      -h|--help) printf "$(cat $CODE_DIR/man.txt)\n\n"; exit 0 ;;
      *) 
        if [ -z $REPO_NAME ]; then 
          REPO_NAME="$1"
        else 
          printf $'\e[31mERROR:\e[0m invalid arg \e[31m'"$1"'\e[0m !\n'
          exit 1
        fi
        shift
        ;;
    esac
  done

  if [ "$CONFIGURE" = true ] ; then
    configure
    exit 0
  fi

  if [ -z $REPO_NAME ]; then
    printf $'\e[31mERROR:\e[0m you must supplay a repository name! '
    printf $'Run \e[32mcreate_project --help\e[0m to get more information.\n'
    exit 1
  else
    if [ ! -f "$CODE_DIR/.env" ]; then
      printf $'Initial configuration :\n'
      configure
    fi
    if [ ! -d "$CODE_DIR/venv" ]; then
      printf $'Configuring python venv (once)\n'
      python3 -m venv $CODE_DIR/venv
      source $CODE_DIR/venv/bin/activate
      pip3 install -r $CODE_DIR/requirements.txt
    fi
    if [ -d "./$REPO_NAME" ]; then
      printf $'\e[31mERROR:\e[0m A directory named \e[34m'"$REPO_NAME"'\e[0m already exists in this folder!\n'
      exit 1
    fi
    export $(grep -v '^#' $CODE_DIR/.env | xargs)
    create_github_repo
    exit 0
  fi
}

configure () {
  read -p $'Enter your \e[1mGitHub Username\e[0m : ' USERNAME
  read -p $'Paste your \e[1mGitHub Personal Access Token\e[0m : ' TOKEN 
  echo "GITHUB_USER=\"$USERNAME\"" > $CODE_DIR/.env
  echo "GITHUB_API_TOKEN=\"$TOKEN\"" >> $CODE_DIR/.env
  printf $'\e[32mConfig saved.\e[0m\n'
}

clone_remote () {
  git clone "https://github.com/$GITHUB_USER/$REPO_NAME.git"
  code ./$REPO_NAME
}

create_github_repo () {

  STATUS_CODE=$($CODE_DIR/venv/bin/python3 $DIR/create_project.py --name $REPO_NAME --description "${REPO_DESCRIPTION}" --license $REPO_LICENSE)

  case "$STATUS_CODE" in 
    "201" ) clone_remote;;
    "422" ) printf $'❌ repository \e[34m'"${REPO_NAME}"$'\e[0m already exists!\n' && exit 1;;
    * ) echo "❌  error: ${STATUS_CODE}" && exit 1;;
  esac
}

main "$@"; exit
