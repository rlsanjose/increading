import priorityqueue, datetime

class Daily_queue:
    
    def __init__(self):
        self.daily_list = []
        self.actual_list = []
        self.current_number = 0

    def order_list(unordered_daily) : 
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
                ordered_daily.append(unordered_daily[item])

            indexes_of_equal_lowest_percentage.reverse()

            for item in indexes_of_equal_lowest_percentage :
                unordered_daily.pop(item)

        return ordered_daily

    def create_daily_list(self, priority_queue):
        
        unordered_daily = []

        # TODO: it is failing here, because "today()" contains the hour, minutes...
        for item in priority_queue.priority_list :
            if item.date_of_next == datetime.date.today():
                unordered_daily.append(item)
            else :
                continue

        ordered_daily = []
        ordered_daily = Daily_queue.order_list(unordered_daily)
        self.daily_list = ordered_daily


    def make_actual_list(self) :
        
        # It's better if we do another list, in case the user wants to repeat the session.
        self.actual_list = self.daily_list

    def consume_one_item(self) :
        
        self.current_number += 1
