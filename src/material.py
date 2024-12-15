import datetime, extractlist, database, file_manager

class Material:

    def __init__(self, material_id, name, author, bookmark, path, 
                 priority_percentage, due_date, review_date, 
                 number_of_reviews, interval_to_next_review, a_factor, is_ended):

        self.id = material_id
        self.name = name
        self.author = author
        self.bookmark = bookmark
        self.path = path

        self.extracts_dir = (self.author + "_" + self.name).replace(" ", "-")
        self.extracts_file_path = self.extracts_dir + "/" + self.extracts_dir + ".md"

        # Date format: string as ISO 8601
        self.review_date = review_date
        self.due_date = due_date
        self.number_of_reviews = number_of_reviews
        self.interval_to_next_review = interval_to_next_review
        self.a_factor = a_factor
        self.priority_percentage = priority_percentage

        self.is_ended = is_ended

# TODO: you create the extract from the material, but then you create the file
# from the extract

# TODO: from here, one should call filemanager.create_singular_directory(),
# which returns the new relative path (which is necessary in case it already
# existed a file with the same name)

# TODO: method: pass itself to database, retrieve and fix the id
 
    def store_in_database(self):
        fm = file_manager.FileManager()
        db = database.Database(fm)
        newid = db.insert_material(self)
        self.id = newid
        return