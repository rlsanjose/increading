import priorityqueue, datetime

class Daily_queue:
    
    def __init__(self):
        self.daily_list = []
        self.actual_list = []
        self.current_number = 0

    def create_daily_list(self, priority_queue):
        
        unordered_daily = priority_queue.priority_list

        for item in priority_queue.priority_list :
            if item.date_of_next == datetime.datetime.today():
                unordered_daily.append(item)
            else :
                continue

        ordered_daily = []

        while True:

            if len(unordered_daily) == 0 :
                break

            lowest_percentage = unordered_daily[0].priority_percentage
            indexes_of_equal_lowest_percentage = []

            for i in range(len(unordered_daily)):

                if unordered_daily[i].priority_percentage < lowest_percentage :
                    lowest_percentage = unordered_daily[i].priority_percentage
                    indexes_of_equal_lowest_percentage = []
                    indexes_of_equal_lowest_percentage.append(i)
                elif unordered_daily[i].priority_percentage == lowest_percentage:
                    indexes_of_equal_lowest_percentage.append(i)
            
            for item in indexes_of_equal_lowest_percentage :
                ordered_daily.append(unordered_daily.pop(item))
        
        self.daily_list = ordered_daily


    def make_actual_list(self) :
        
        # It's better if we do another list, in case the user wants to repeat the session.
        self.actual_list = self.daily_list

    def consume_one_item(self) :
        
        self.current_number += 1
        self.actual_list.pop(0)
