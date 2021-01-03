# Put this function in your ~/.bashrc or ~/.zshrcfile! 
# Be sure to replace the path to the `main.py` script with yours.

function create_project () {
    python3 path/to/project_generator/src/main.py "$@"
}
