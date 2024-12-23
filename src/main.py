import priorityqueue
import file_manager
import database
import dailyqueue
import material
import extract
import datetime
import os


def start_session():

    priority_queue = priorityqueue.Priority_queue()
    priority_queue.retrieve_list_of_items()
    if len(priority_queue.priority_list) == 0:
        print("\nEmpty list. Start by adding materials!\n")
        input("Press enter to continue\n")
        return
    daily_queue = dailyqueue.Daily_queue()
    daily_queue.create_daily_list(priority_queue)
    if len(daily_queue.daily_list) == 0:
        print("\nNothing to review today :(\n")
        input("Press enter to continue\n")
        return
    daily_queue.make_actual_list()

    for item in daily_queue.actual_list:

        os.system("cls|clear")
        # while True:
        #     if not daily_queue.current_number < len(daily_queue.actual_list):
        #         os.system("cls|clear")
        #         input("\n\nThe daily queue is ended.\n\nPress enter to continue")
        #         break
        print(
            "\n"
            + str(daily_queue.current_number + 1)
            + " / "
            + str(len(daily_queue.actual_list))
        )
        print("\n")

        if isinstance(item, material.Material):
            print(item.author + ": " + item.name)
            print("\n")
            print("Go to: " + item.path)
            print("\n")
            while True:
                some_options = input(
                    "Select option: \n"
                    + "    (a) Mark as reviewed\n"
                    + "    (b) Add new extract\n"
                    + "    (c) Pospone material\n"
                    + "    (d) Mark as ended\n"
                    + "    (e) Interrupt here\n"
                    + "Enter: "
                )
                match some_options:
                    case "a" | "A":
                        # Set new bookmark
                        new_bookmark = input("Enter new bookmark: ")
                        item.review_material(new_bookmark)
                        break
                    case "b" | "B":
                        extract_id = 0
                        material_id = item.id
                        bookmark = input("Enter page of book: ")
                        path = ""
                        review_date = datetime.date.today().isoformat()
                        due_date = review_date
                        number_of_reviews = 0
                        interval_to_next_review = 1
                        a_factor = 2.5
                        priority_percentage = item.priority_percentage
                        is_suspended = 0
                        material_extracts_dir = item.extracts_dir
                        new_extract = extract.Extract(
                            extract_id,
                            material_id,
                            bookmark,
                            path,
                            review_date,
                            due_date,
                            number_of_reviews,
                            interval_to_next_review,
                            a_factor,
                            priority_percentage,
                            is_suspended,
                            material_extracts_dir,
                        )
                        # Schedule
                        new_extract.review_extract(0)
                        # Store in db
                        new_extract.store_in_database()
                        # Create file and edit
                        new_extract.create_and_edit_extract(item)
                        continue
                    case "c" | "C":
                        while True:
                            num_of_days = input("Days to pospone: ")
                            if num_of_days.isdecimal():
                                item.pospone(int(num_of_days))
                                break
                            else:
                                print("\nInvalid input\n")
                            continue
                        break
                    case "d" | "D":
                        item.end_material()
                        break
                    case "e" | "E":
                        item.pospone(1)
                        daily_queue.current_number = len(daily_queue)
                        break
                    case _:
                        print("\nInvalid input\n")
                        continue
        elif isinstance(item, extract.Extract):
            os.system("cls|clear")
            item.edit_extract()
            os.system("cls|clear")
            while True:
                some_options = input("Select an option: \n"
                                     + "    (a) Mark as reviewed\n"
                                     + "    (b) Edit again\n"
                                     + "    (c) Pospone X days\n"
                                     + "    (d) Mark as ended/suspended\n"
                                     + "Enter: ")
                match some_options:
                    case "a":
                        while True:
                            punctuation = input(
                                "\nEnter your punctuation (0 to reset the schedule, 1 to keep spacing): ")
                            if punctuation.isdecimal():
                                break
                            else:
                                print("\nInvalid input\n")
                                continue
                        item.review_extract(int(punctuation))
                        break
                    case "b":
                        item.edit_extract()
                        os.system("cls|clear")
                        continue
                    case "c":
                        while True:
                            options = input("Days to pospone: ")
                            if options.isdecimal():
                                break
                            else:
                                print("\nInvalid input\n")
                                continue
                        item.pospone_extract(int(num_of_days))
                        pass
                    case "d":
                        item.end_extract()
                        break
                    case _:
                        print("\nInvalid input\n")
                        continue
        daily_queue.consume_one_item()
        continue


def add_material():
    name = input("Name: ")
    author = input("Author: ")
    path = input("Path: ")
    bookmark = "Start"
    extracts_dir = ""
    extracts_file_path = ""
    review_date = material.Material.get_first_date()
    due_date = review_date
    number_of_reviews = 0
    interval_to_next_review = 1
    a_factor = 1
    is_ended = 0
    while True:
        priority_percentage = input(
            "Priority percentage (0-100)\n"
            + "[Caution: 0 is the highest priority, 100 is the lowest]\n"
            + "Enter: "
        )
        if priority_percentage.isdecimal():
            priority_percentage = int(priority_percentage)
            break
        else:
            print("\nInvalid input\n")
            continue

    new_material = material.Material(
        0,
        name,
        author,
        path,
        bookmark,
        extracts_dir,
        extracts_file_path,
        review_date,
        due_date,
        number_of_reviews,
        interval_to_next_review,
        a_factor,
        priority_percentage,
        is_ended
    )
    new_material.add_new_material()
    return


def see_queue():
    queue = priorityqueue.Priority_queue()
    queue.retrieve_list_of_items()
    index = 0
    print(
        "------------------------------\n\
Place--Priority--Title--Author\n\
------------------------------"
    )
    queue2 = []
    for item in queue.priority_list:
        if isinstance(item, material.Material):
            queue2.append(item)

    queue2.sort(key=lambda x: x.priority_percentage)
    for item in queue2:
        print(index, ":", item.priority_percentage,
              "\b%", item.name, item.author)
        index += 1


os.system("cls|clear")
print("\nWelcome to increading\n")


while True:
    text = "\nSelect an option:\n\
    (a) Start session\n\
    (b) Add material\n\
    (c) See Priority List\n\
    (e) ¿First time? Create directories, config file and database\n\
    (f) Exit\n"

    option = input(text)

    match option:
        case "a" | "A":
            start_session()
        case "b" | "B":
            add_material()
        case "c" | "C":
            see_queue()
            pass
        case "d" | "D":
            see_queue()
            input("\n(press enter)\n")
        case "e" | "E":
            fm = file_manager.FileManager()
            if not fm.check_user_config_dir():
                fm.create_user_config_dir()
                print("\nConfig dir created")
            if not fm.check_config_file():
                fm.create_config_file()
                print("\nConfig file created")
            if not fm.check_user_data_dir():
                fm.create_user_data_dir()
                print("\nData dir created")
            if not fm.extracts_directory_exists():
                fm.create_extracts_directory()
                print("\nExtracts dir created")
            db = database.Database(fm)
            con, cur = db.connect_database()
            con.close()
            print("\nDatabase created")
            # Create tables
            db.create_tables()
            print("\nTables created")
            continue

        case "f" | "F":
            break
        case _:
            a = input("\nError: invalid. Press enter\n")
