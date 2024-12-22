import datetime
import file_manager
import database
import schedule


class Extract:

    # Instead of passing the material object, I will pass the values
    # (material_id and material_extracts_dir).

    def __init__(
        self,
        extract_id,
        material_id,
        bookmark,
        path,
        review_date,
        due_date,
        number_of_reviews,
        interval_to_next_review,
        a_factor,
        priority_percentage,
        is_suspended,
        material_extracts_dir="",
    ):

        self.extract_id = extract_id
        self.material_id = material_id
        self.bookmark = (bookmark,)

        # Saving the path with the current date
        # TODO: When creating a new extract, check if this file already exists
        # and rename
        if path == "":
            instant = datetime.datetime.now()
            instant_str = (
                str(instant.year)
                + str(instant.month)
                + str(instant.day)
                + "-"
                + str(instant.hour)
                + str(instant.minute)
                + str(instant.second)
            )
            self.path = material_extracts_dir + "/" + instant_str + ".md"

        self.review_date = review_date
        self.due_date = due_date
        self.number_of_reviews = number_of_reviews
        self.interval_to_next_review = interval_to_next_review
        self.a_factor = a_factor
        self.priority_percentage = priority_percentage
        self.is_suspended = is_suspended

    def store_in_database(self):
        fm = file_manager.FileManager()
        db = database.Database(fm)
        newid = db.insert_extract(self)
        self.extract_id = newid
        return

    def review_extract(self, punctuation: int):
        # Set new review date
        self.review_date = datetime.date.today().isoformat()
        # New due date and interval
        new_interval, new_due_date = schedule.Scheduler.review(
            self.review_date, self.a_factor, self.interval_to_next_review, punctuation
        )
        self.interval_to_next_review = new_interval
        self.due_date = new_due_date
        # Update database
        fm = file_manager.FileManager()
        db = database.Database(fm)
        db.update_extract_review_and_due_dates()
        db.update_extract_interval_to_next_review()
        return

    def pospone_extract(self, num_of_days: int = 1):
        self.due_date = (datetime.date.today() +
                         datetime.timedelta(num_of_days)).isoformat()
        fm = file_manager.FileManager()
        db = database.Database(fm)
        db.update_extract_review_and_due_dates()
        return

    def end_extract(self):
        self.is_suspended = 1
        fm = file_manager.FileManager()
        db = database.Database(fm)
        db.update_extract_is_suspended()
        return
