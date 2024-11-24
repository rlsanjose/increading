import material, datetime

class Extract:

    def __init__(self, extract_id, material):
        self.extract_id = extract_id
        self.material = material
        self.priority_percentage = material.priority_percentage

