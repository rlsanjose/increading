from pathlib import Path
import os
import material
import configparser
import extract


class FileManager:

    def __init__(self):
        self.home_dir = Path.home()
        self.user_data_dir = os.path.expanduser("~/.local/share/increading")
        self.db_path = self.user_data_dir + "/database.sqlite"
        self.user_config_dir = os.path.expanduser("~/.config/increading")
        if self.check_config_file():
            self.retrieve_extract_path()
        else:
            # Temporary solution, set a new extracts_path after creating this
            # object but before creating the config file
            self.extracts_path = os.path.expanduser("~/increading")

    """
        All the previous paths need to be absolute
    """

    def extracts_directory_exists(self):
        if self.extracts_path == "":
            return False
        elif os.path.exists(self.extracts_path):
            return os.path.isdir(self.extracts_path)
        else:
            return False

    # This is returning an absolute path.
    def create_directory(self, path_string: str) -> str:
        # We'll asume we are getting the parent directory
        path_expanded = os.path.expanduser(path_string)
        path = Path(path_expanded)
        try:
            # Commenting the next line because of repeated action
            # Path(path).mkdir(parents=True, exist_ok=False)
            os.mkdir(path_expanded)
        except FileExistsError:
            if path.is_dir():
                return path_expanded
            else:
                newdir = path_expanded + "_dir"
                # TODO: Check if this works.
                new_newdir = self.create_directory(newdir)
                return new_newdir
        except Exception:
            return "Error"
        return path_expanded

    def create_extracts_directory(self) -> bool:
        try:
            new_dir = self.create_directory(self.extracts_path)
            return True
        except Exception:
            return False

    def create_singular_directory(self, material: material.Material) -> str:
        relative_path = material.extracts_dir
        absolute_path = self.extracts_path + "/" + relative_path
        # TODO: Check if the next works
        while os.path.exists(absolute_path):
            absolute_path += "_new"
            relative_path += "_new"
        self.create_directory(absolute_path)
        # returns new_path so the material can save its path
        return relative_path

    # TODO: not sure if `exists()` works here.
    # TODO: Extracts_path needs to be a string with an absolute path
    def check_singular_directory(self, material: material.Material):
        new_path = self.extracts_path + "/" + material.extracts_dir
        return new_path.exists()

    def check_user_data_dir(self):
        return self.user_data_dir.exists()

    def create_user_data_dir(self):
        self.create_directory(self.user_data_dir)
        return

    def check_user_config_dir(self):
        return self.user_config_dir.exists()

    def create_user_config_dir(self):
        self.create_directory(self.user_config_dir)
        self.create_config_file()
        return

    # Remember to set `self.extracts_path` before creating the config file
    def create_config_file(self):
        config_file_path = self.user_config_dir + "/increading.config"
        config_file = configparser.ConfigParser()
        config_file["general"] = {
            "extracts_dir": self.extracts_path,
            "db_dir": self.user_data_dir,
        }
        with open(config_file_path, "w") as configfile:
            config_file.write(configfile)

    def check_config_file(self):
        config_file_path = self.user_config_dir + "/increading.config"
        return os.path.exists(config_file_path)

    # If config_file is created, then we don't need to check if there is
    # 'general.extracts_path'

    # Extracts_path needs to be a string with an absolute path
    def retrieve_extract_path(self):
        config_file_path = self.user_config_dir + "/increading.config"
        config_file = configparser.ConfigParser()
        config_file.read(config_file_path)
        new_extracts_dir = config_file["general"]["extracts_dir"]
        self.extracts_path = new_extracts_dir
        return

    def check_db(self):
        return os.path.exists(self.db_path)

    def create_singular_extract_file(self, extract: extract.Extract, name, author, bookmark) -> str:
        new_path = self.extracts_path + "/" + extract.path
        f = open(new_path, "w")
        first_line = "# " + name + ", " + author + ", " + bookmark
        f.write(first_line)
        f.write("\n")
        f.close()
        return new_path

    def create_extract_list_file(self, material: material.Material):
        new_path = self.extracts_path + "/" + material.extracts_file_path
        first_line = "# " + material.name + ", " + material.author
        try:
            create_file = open(new_path, "x")
            create_file.close()
        except Exception:
            pass
        with open(new_path, "a") as f:
            f.write(first_line)
            f.write("\n")
        return

    def concat_extract_to_list(
        self, material: material.Material, extract: extract.Extract
    ):
        extract_list_path = self.extracts_path + "/" + material.extracts_file_path
        singular_extract_path = self.extracts_path + "/" + extract.path
        file2 = open(singular_extract_path, "r")
        text = file2.read()
        file2.close()
        file1 = open(extract_list_path, "a")
        file1.write("\n" + "---" + "\n")
        file1.write(text)
        file1.close()
        return


# TODO: I should create a method to get the extract list whole path, to be able
# to reuse it. The same with singular extracts.

# TODO: create a method that groups the methods necessary when opening the app
# for the first time: creating the config file, the directories, the db...
# Or maybe create a new class for this?
