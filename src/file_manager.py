from pathlib import Path
import os
import material
import configparser

class FileManager :

    def __init__(self):
        self.home_dir = Path.home()
        self.user_data_dir = os.path.expanduser("~/.local/share/increading")
        self.user_config_dir = os.path.expanduser("~/.config/increading")
        self.extracts_path = ""

    def set_extracts_path(self, absolute_path : str) :
        self.extracts_path = absolute_path

    # TODO: check if the next function actually works. I recently changed
    # `self.extracts_path.exists()` to `os.path.exists(str)`. The first would
    # only work with Path object

    def extracts_directory_exists(self):
        if self.extracts_path == "" :
            return False
        elif os.path.exists(self.extracts_path):
            return os.path.isdir(self.extracts_path)
        else:
            return False

    def create_directory(self, path_string : str) -> Path:
        # Fails when it has to create a parent directory, but a file exist with the
        # same name as the parent
        
        path_expanded = os.path.expanduser(path_string)
        path = Path(path_expanded)
        try:
            Path(path).mkdir(parents=True, exist_ok=False)
            os.mkdir(path)
        except FileExistsError:
            if path.is_dir():
                return path_expanded
            else:
                newdir = path_expanded + "_dir"
                self.create_directory(newdir)
                return newdir
        except Exception:
            return path_expanded
        return path_expanded

    def create_extracts_directory(self) -> bool:
        try:
            new_dir = self.create_directory(self.extracts_path)
            return True
        except Exception:
            return False

    def create_singular_directory(self, material : material.Material) -> str:
        new_rel_path = material.author + "_" + material.name
        new_rel_path.replace(" ", "-")
        while self.check_singular_directory():
            new_path += "_new"
        self.create_directory(self.extracts_path + "/" + new_path)
        # returns new_path so the material can save its path
        return new_path
    
    def check_singular_directory(self, material :material.Material):
        new_path = self.extracts_path + "/" + material.extracts_dir
        return new_path.exists()

    def check_user_data_dir(self):
        return self.user_data_dir.exists()

    def create_user_data_dir(self) :
        self.create_directory(self.user_data_dir)
    
    def check_user_config_dir(self):
        return self.user_config_dir.exists()

    def create_user_config_dir(self) :
        self.create_directory(self.user_config_dir)
        self.create_config_file()

    def create_config_file(self):
        config_file_path = self.user_config_dir + "/increading.config"
        config_file = configparser.ConfigParser()
        config_file["general"] = {'extracts_dir' : self.extracts_path, 
                                  'db_dir' : self.user_data_dir}
        with open(config_file_path, 'w') as configfile:
            config_file.write(configfile)
    
    def check_config_file(self):
        config_file_path = self.user_config_dir + "/increading.config"
        return os.path.exists(config_file_path)

    def retrieve_extract_path(self):
        config_file_path = self.user_config_dir + "/increading.config"
        config_file = configparser.ConfigParser()
        config_file.read(config_file_path)
        new_extracts_dir = config_file['general']['extracts_dir']
        self.set_extracts_path(new_extracts_dir)

# TODO: I need this functions: 
#     - [X](1) create_extract_directory (the general one),
#     - [X] (2) check if that directory exists, 
#     - [X] (3)&(4) the same with the individual extract folders and subfolders,
#     - [X] (5)&(6) the same with the .local/share directory, 
#     - [ ] (7) maybe even check if a database exist, 
#     - [X] (8)&(9) checking and creating a config file where we'll save where
#       the database is (just in case) and where the extract directory is.
#     - [ ] (10) create a file for extract_list
#     - [ ] (11) create a file for singular_extract


# Take into account: make a general function (check_or_create_dir()) who then
# can serve to create the different directories, whose paths can be saved as
# variables in this module.