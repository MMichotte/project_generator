"""
@Author: Martin Michotte
"""

class Repository():
    """
    docstring
    """
    def __init__ (self, name, description, with_readme, license_template, git_ignore_template, is_private):
        self.name = name
        self.description = description
        self.license_template = license_template
        self.gitignore_template = git_ignore_template
        self.private = is_private
        self.auto_init = with_readme

    def __repr__ (self):
        return self.name

    def get_json (self):
        json = {}
        for attr, val in self.__dict__.items():
            if val is not None:
                json[attr] = val
        return json
