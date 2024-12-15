from operator import attrgetter


class Priority_queue:

    def __init__(self):
        self.priority_list = []
    

    def add_item(self, item):
        self.priority_list.append(item)

    def order_list(self):
        
        if len(self.priority_list) == 0 :
            return
        
        self.priority_list.sort(key=attrgetter("priority_percentage"))
    
    # TODO: retrieve list of materials and extracts from database

        