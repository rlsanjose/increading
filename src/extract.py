import material
import datetime
import file_manager
import database


class Extract:

    # Instead of passing the material object, I will pass the values.

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
            self.path = material.extracts_dir + "/" + instant_str + ".md"

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
