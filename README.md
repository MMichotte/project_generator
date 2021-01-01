# project_generator

🚀 Simple bash & python script that enables you to create a new project folder with its new github repository.

## Description :
`Project_generator` enables you to create a new project folder and the corresponding git repository in just one command. 
#### What does it really do ? 
1. Using the Github API it creates a new Github Repository with a given **name**, **description** (*optional*), a **README** file and the **MIT licence**.
2. Clones the newly created Github Repository in your local folder.
3. Opens your new project in `VsCode`. 

## Setup : 
1. Download/clone this repository and save it somewhere on your computer. 
2. Modify and copy the content of the `.zshrc` file from this repository to your `.bashrc`or `.zshrc`file.
3. Get your `Github Access Token` ([how to get one?](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)) (⚠️ You must at least give all the `repository privileges` to your token)
4. Update the `.env`file with your `Github Username` and the newly created `access token`.
   
## Usage :
1. Navigate to the root folder in which you want to create a new project. 
2. Run :
   ```bash
   create_project my_new_project "the project description."
   ```
