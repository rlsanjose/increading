import material, datetime

class Extract:

    def __init__(self, extract_id, materia : material.Material):
        self.extract_id = extract_id
        self.material = material
        self.priority_percentage = material.priority_percentage
        self.path = material.extracts_dir + "/" + self.extract_id + ".md"

