import material, datetime

class Extract:

    def __init__(self, extract_id, material : material.Material):
        self.extract_id = extract_id
        self.material_id = material.id
        #self.material = material
        self.priority_percentage = material.priority_percentage
        self.path = material.extracts_dir + "/" + self.extract_id + ".md"
        # TODO:
        self.next_repetition_date = ""
        self.number_of_repetitions = 0
        self.days_between_repetitions = 1

