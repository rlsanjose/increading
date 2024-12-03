import material, datetime

class Extract:

    def __init__(self, extract_id, material : material.Material, bookmark, review_date, due_date,
                 number_of_reviews, interval_to_next_review, a_factor):
        self.extract_id = extract_id
        self.material_id = material.id
        self.bookmark = bookmark,
        self.path = material.extracts_dir + "/" + self.extract_id + ".md"

        self.review_date = review_date
        self.due_date = due_date
        self.number_of_reviews = number_of_reviews
        self.interval_to_next_review = interval_to_next_review
        self.a_factor = a_factor
        self.priority_percentage = material.priority_percentage

