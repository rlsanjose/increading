class Priority_queue:

    def __init__(self):
        self.priority_list = []
    

    def add_item(self, item):
        self.priority_list.append(item)

    # TODO: Will it be really necessary to order this list?

    def order_list(self):

        unordered_list = self.priority_list
        ordered_list = []
        
        while True :

            if len(unordered_list) == 0 :
                break

            lowest_percentage = unordered_list[0].priority_percentage
            indexes_of_equal_lowest_percentage = []

            for i in range(len(unordered_list)):
                if unordered_list[i].priority_percentage < lowest_percentage :
                    lowest_percentage = unordered_list[i].priority_percentage
                    indexes_of_equal_lowest_percentage = []
                    indexes_of_equal_lowest_percentage.append(i)
                elif unordered_list[i].priority_percentage == lowest_percentage:
                    indexes_of_equal_lowest_percentage.append(i)

            for item in indexes_of_equal_lowest_percentage :
                ordered_list.append(unordered_list.pop(item))

        self.priority_list = ordered_list