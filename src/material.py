import datetime
import extractlist
import database
import file_manager


class Material:

    def __init__(
        self,
        material_id,
        name,
        author,
        path,
        bookmark,
        extracts_dir,
        extracts_file_path,
        review_date,
        due_date,
        number_of_reviews,
        interval_to_next_review,
        a_factor,
        priority_percentage,
        is_ended,
    ):

        self.id = material_id
        self.name = name
        self.author = author
        self.bookmark = bookmark
        self.path = path
        # The next paths are relative paths to the materials directory.
        # Pass empty strings when creating new material
        if extracts_dir == "":
            self.extracts_dir = (self.author + "_" +
                                 self.name).replace(" ", "-")

        if extracts_file_path == "":
            self.extracts_file_path = (
                self.extracts_dir + "/" + self.extracts_dir + ".md"
            )

        # Date format: string as ISO 8601
        self.review_date = review_date
        self.due_date = due_date
        self.number_of_reviews = number_of_reviews
        self.interval_to_next_review = interval_to_next_review
        self.a_factor = a_factor
        self.priority_percentage = priority_percentage

        self.is_ended = is_ended

    # TODO: you create the extract from the material, but then you create the
    # file from the extract

    # This method groups the necessary methods to generate the material
    # directory and extracts file when creating a new material.
    def create_material_dirs_and_files(self):
        fm = file_manager.FileManager()
        # We assume there already is a config file
        fm.retrieve_extract_path()
        # Create the directory
        new_extracts_dir = fm.create_singular_directory(self)
        if new_extracts_dir != self.extracts_dir:
            self.extracts_dir = new_extracts_dir
            # Update the database to set the new path
            db = database.Database(fm)
            db.update_material_extracts_dir(self)
        # Create the extract list file
        fm.create_extract_list_file(self)
        return

    def store_in_database(self):
        fm = file_manager.FileManager()
        db = database.Database(fm)
        newid = db.insert_material(self)
        self.id = newid
        return
