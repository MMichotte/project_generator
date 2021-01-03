# project_generator

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/MMichotte/US-to-TrelloCard/blob/main/LICENSE) [![Generic badge](https://img.shields.io/badge/Python-3.7-blue.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/platform-osx_|_linux_|_win-white.svg)](https://shields.io/)


`Project_generator` enables you to create a new project folder and the corresponding Github repository in just one command. 
#### What does it really do ? 
1. Using the Github API it creates a new Github Repository with your new project's name and a few options such as a license, a readme file and more. 
2. Clones the newly created Github Repository in your local folder.
3. Opens your new project in `VsCode`. 

## Setup : 
❗️ You must have `python3`installed on your machine! 

1. Download/clone this repository and save it somewhere on your computer. 
2. Modify and copy the content of the `.zshrc` file from this repository to your `.bashrc`or `.zshrc`file.
3. Get your `Github Access Token` ([how to get one?](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)) (⚠️ You must at least give all the `repository privileges` to your token)
4. Run configuration 
   ```bash
   create_project --config 
   ```
5. You're ready to start using this script. Use `create_project --help` to get more information. 
   
## Usage :
1. Navigate to the root folder in which you want to create a new project. 
2. Run :
   ```bash
   create_project my_new_project -d "the project description." 
   ```


## Manpage :
```bash
NAME
    create_project - create a new project folder and the corresponding public repository.

SYNOPSIS
    create_project [NEW-PROJECT-NAME]... [OPTION]... 

OPTIONS

    -d, --description       Add a description to your Github repository.
                            Your description will also be written in your README file

    -l, --license           Add a Github license to your project. DEFAULT=mit 
                            Available: see < Github license list >
                            DEFAULT= /

    -gi, --gitignore        Add a .gitignore file from a given template.
                            Available: see < Github gitignore template list >
                            DEFAULT= / 

    -nr, --no-readme        Don\'t add a readme file on creation. 

    -p, --private           Make this repository private on Github.

    -c, --config            Configure your GitHub credentials.
    
    --config-defaults       Configure a default value for the licence and gitignore.

    -h, --help              Display the help page.


EXAMPLES
    The command:
    
        create_project my_new_project 

    will create a new Github repository named "my_new_project"
    and clone it on your local machine.


    The command:

        create_project my_new_project -d "a beautiful description"

    will create a new Github repository named "my_new_project" 
    with as description "a beautiful description" and clone it on your local machine.

    The command:

        create_project my_new_project -d "a beautiful description" -l gpl-3.0 -gi Python -p 

    will create a new private Github repository named "my_new_project" 
    with as description "a beautiful description", a gpl-3.0 license (GNU General Public License), 
    a Python .gitignore file and clone it on your local machine.

```