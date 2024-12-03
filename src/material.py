import datetime, extractlist

class Material:

    # TODO: Rethink the arguments its receiving...

    def __init__(self, material_id, name, author, path, priority_percentage, due_date, review_date, a_factor):
        self.id = material_id
        self.name = name
        self.author = author
        self.bookmark = ""
        self.path = path

        self.extracts_dir = (self.author + "_" + self.name).replace(" ", "-")
        self.extracts_file_path = self.extracts_dir + "/" + self.extracts_dir + ".md"

        self.review_date = review_date
        self.due_date = due_date
        self.number_of_reviews = 0
        self.interval_to_next_review = 1
        self.a_factor = a_factor
        self.priority_percentage = priority_percentage

        self.is_ended = 0
        # Change: is better to save the date, not the resting days
        # self.days_to_next = 1
        # self.days_since_last = 0
        # self.type = type
        # self.extracts = []
        #TODO:    self.priority_num 
        # Not sure if we need a priority_num. It's just its index in priority queue.
        # Doesn't even need that field in the db

    def set_bookmark(self, bookmark):
        self.bookmark = bookmark

    def change_name(self, new):
        self.name = new

    def change_author(self, new):
        self.author = new

# TODO: this also needs to change: we are not getting the numbers of days left but the date
    #def pospone_material(self, new):
        #self.days_to_next = new

    def change_interval(self, new):
        self.interval_to_next_review = new

    def change_a_factor(self, new):
        self.a_factor = new
    
    # TODO: change_priority: change priority index by checking the priority queue
    
    def change_priority(self, new):
        self.priority_percentage = new
        # After this, it is necessary to call the order_list method
        # TODO: change also in the priority queue
        # self.priority_num

    # TODO: The next is not correct. Needs a rethinking of the problem
    # update interval after a repetition
    # def update_interval(self):
    #     self.repetition_interval *= self.a_factor

    # This is not correct
    # def next_interval(self):
    #     self.days_to_next = self.repetition_interval * self.a_factor

    # def days_passing(self, days):
    #     self.days_to_next -= days
    #     if self.days_to_next > 0:
    #         self.days_to_next = 0

    # def add_extract(self, extract):
    #     self.extracts.append(extract)

# TODO: you create the extract from the material, but then you create the file
# from the extract

# TODO: from here, one should call filemanager.create_singular_directory(),
# which returns the new relative path (which is necessary in case it already
# existed a file with the same name)