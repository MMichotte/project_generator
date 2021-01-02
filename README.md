# project_generator

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/MMichotte/US-to-TrelloCard/blob/main/LICENSE) [![Generic badge](https://img.shields.io/badge/Python-3.8-purple.svg)](https://shields.io/)


`Project_generator` enables you to create a new project folder and the corresponding git repository in just one command. 
#### What does it really do ? 
1. Using the Github API it creates a new Github Repository with a given **name**, **description** (*optional*), a **README** file and by default the **MIT licence**.
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
