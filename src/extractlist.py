# The extract_list is a file with all the extracts, as they are written while reading.
# Not to be confused with the series of single extract files that are being processed.

class Extract_list :
    
    def __init__(self, material):
        self.material = material
        self.extracts = []
        self.path = self.material.name.replace(" ", "-").lower()+".md"

    def create_new_file(self):
        extract_list_file = open(self.path, "w")
        extract_list_file.write(self.material.name)
        extract_list_file.close()

    def open_file(self):
        pass


# TODO:    def get_individual_extracts(self):