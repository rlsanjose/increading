import database
import file_manager
import datetime
import schedule


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

        # Is_ended is 0 if it is not ended, and 1 if it is
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

    """
        When creating a new material, I will call the next static method to
        get what I need to asign to review and due date = tomorrow. (In case
        the user want to pospone, it can be done later.) After that, I will
        call the constructor with those values. Then, I will call
        `add_new_material` to create the dirs and save in the db.
    """

    @staticmethod
    def get_first_date():
        return (datetime.date.today() + datetime.timedelta(1)).isoformat()

    def add_new_material(self):
        # Create dir and file
        self.create_material_dirs_and_files()
        # Store in database
        self.store_in_database()
        return

    def review_material(self, new_bookmark: str):
        # Set new bookmark
        self.bookmark = new_bookmark
        # Update database: bookmark
        fm = file_manager.FileManager()
        db = database.Database(fm)
        db.update_material_bookmark(self)
        # Set new review date
        self.review_date = datetime.date.today().isoformat()
        # Set due date and new interval
        (new_due_date, new_interval) = schedule.Scheduler.review(
            self.review_date, self.a_factor, self.interval_to_next_review, 1)
        self.due_date = new_due_date
        self.interval_to_next_review = new_interval
        # Update database: review and due date
        db.update_material_review_due_dates(self)
        # Add a review
        self.number_of_reviews += 1
        db.update_material_number_of_reviews(self)
        return

    def pospone(self, num_of_days: int = 1):
        interval = datetime.timedelta(num_of_days)
        actual_date = datetime.date.today()
        next_date = actual_date + interval
        self.due_date = next_date.isoformat()
        return

    def end_material(self):
        self.review_date = datetime.date.today().isoformat()
        fm = file_manager.FileManager()
        db = database.Database(fm)
        db.update_material_review_due_dates(self)
        self.is_ended = 1
        db.update_material_is_ended()
        return
