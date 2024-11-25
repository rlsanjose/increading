import priorityqueue, dailyqueue, material, extract, datetime, os

os.system('cls|clear')
print("Welcome to increading\n")

actual_date = datetime.date.today()

date_text = actual_date.strftime("%d/%m/%Y")

print(date_text, "\n")

priority_queue = priorityqueue.Priority_queue();

def start_session():

    daily_queue = dailyqueue.Daily_queue()
    daily_queue.create_daily_list(priority_queue)
    daily_queue.make_actual_list()


    for item in daily_queue.actual_list :
        
        os.system('cls|clear')
        while True :
            print(str(daily_queue.current_number + 1) + " / " + str(len(daily_queue.actual_list)))
            print("\n")
            print(item.author + ": " + item.name)
            print("\n")
            print("Go to: " + item.path)
            print("\n")
            some_options = input ("Select option: \n" +
                                "    (a) Open extracts\n" + 
                                "    (b) Pospone material\n" +
                                "    (c) Set new bookmark and go to the next material\n" +
                                "    (d) Interrupt here\n")
            match some_options :
                case "a"|"A" :
                    item.create_extract_list()
                    item.extract_list.create_new_file()
                    os.system("vim " + item.extract_list.path)
                
                case "b"|"B" :
                    pass
                case "c"|"C" : 
                    pass
                case "d"|"D" : 
                    pass


        daily_queue.consume_one_item()
        continue


def add_material():
    type = ""
    options = input("Enter type:\n\
(a) pdf\n\
(b) web-page\n\
(c) physical\n\
(d) plain text\n\
(e) epub\n\
(f) other\n")
    match options:
        case "a"|"A"|"pdf":
            type = "pdf"
        case "b"|"B"|"web-page":
            type = "web"
        case "c"|"C"|"physical":
            type = "physical"
        case "d"|"D"|"plain text":
            type = "plain-text"
        case "e"|"E"|"epub":
            type = "epub"
        case _ :
            type = "other"
    name = input("Name: ")
    author = input("Author: ")
    path = input("Path: ")
    priority_percentage = int(input("Priority percentage (0-100)\n[Caution: 0 is the highest priority, 100 is the lowest]\n"))
    if priority_percentage > 100 :
        priority_percentage = 100
    elif priority_percentage < 0 :
        priority_percentage = 0
    a_factor = 1
    how_many_days = 0
    configure_more = input("Do you want to configure further (pospone, a-factor)? (Y/N)")
    date_to_show = actual_date
    if configure_more == "Y" or configure_more == "y" :
        how_many_days = int(input("How many days to pospone: "))
        date_to_show = actual_date + datetime.timedelta(days=how_many_days)
        print("Next review set to", date_to_show.strftime("%d/%m/%Y"))
        a_factor = float(input("Select A-Factor: (float over 1.0) "))

    # TODO: add verification to this steps
    # TODO: correct the material_id thing

    new_material = material.Material(8, type, name, author, path, priority_percentage, date_to_show, a_factor)
    priority_queue.add_item(new_material)
    priority_queue.order_list()

    wait = input("\nAdded... Press enter to continue\n")
    return


def see_queue() :
    index = 0
    print("------------------------------\n\
Place--Priority--Title--Author\n\
------------------------------")
    for item in priority_queue.priority_list :
        print(index, ":", item.priority_percentage, "\b%", item.name, item.author)
        index += 1
    
    false_input = input("\nPress enter to continue...")

while True:
    text = "\nSelect an option:\n\
    (a) Start session\n\
    (b) Add material\n\
    (c) Browse materials and extracts\n\
    (d) See Priority List\n\
    (e) Exit (changes will be saved)\n" 
    
    option = input(text)

    match option:
        case "a"|"A":
            start_session()

        case "b"|"B":
            add_material()
        case "c"|"C":
            pass
        case "d"|"D":
            see_queue();
        case "e"|"E":
            break
        case _:
            a = input("\nError: invalid. Press enter\n")

