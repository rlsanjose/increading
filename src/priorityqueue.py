from operator import attrgetter
import database
import file_manager


class Priority_queue:

    def __init__(self):
        self.priority_list = []

    def add_item(self, item):
        self.priority_list.append(item)

    def order_list(self):

        if len(self.priority_list) == 0:
            return

        self.priority_list.sort(key=attrgetter("priority_percentage"))

    # Retrieve list of materials and extracts from database

    def retrieve_list_of_items(self):
        fm = file_manager.FileManager()
        db = database.Database(fm)
        material_list = db.read_all_materials()
        extract_list = db.read_all_extracts()
        new_list = material_list + extract_list
        self.priority_list = new_list
        return
