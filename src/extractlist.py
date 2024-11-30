# The extract_list is a file with all the extracts, as they are written while reading.
# Not to be confused with the series of single extract files that are being processed.

import os


class Extract_list :
    
    def __init__(self, material):
        self.material = material
        self.extracts = []
        self.path = ""
        self.dir_name = self.material.name.replace(" ", "-").lower()
        self.file_name = self.material.name.replace(" ", "-").lower()+".md"

# Not really sure if this objects needs to propagate the general path, or if it
# can just take it (as in "material.path").

    #TODO
    def create_new_dir(self):
        os.mkdir(path + self.dir_name)


    def create_new_file(self):
        extract_list_file = open(self.path + self.file_name, "w")
        extract_list_file.write(self.material.name)
        extract_list_file.close()

    def open_file(self):
        pass

    #TODO

    def check_existing_file(self) :
        pass


# TODO:    def get_individual_extracts(self):