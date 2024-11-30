# increading

A simple CLI incremental reading app.

## TODO: basic functionality

- [X] Add type to Materials (pdf, web, epub...)
- [X] Add extract list to materials (has to be another object)
- [X] Replace loops with min function. Better: use sort function
- [X] Add functionality to add extracts during session
    - [X] For now, I can hard-code it to work with vim (look later vim
    sessions...). Later, we will let the user decide.

- [X] Create path variables for extract_list and extract
    - [X] Path for the database: ~/.local/share/increading/database.sqlite
    - [X] Path for the extracts.
        - [X] Also, the path where this config is going to be saved. Don't
        really know where should it be, maybe
            - ~/.config/increading
            - Or I can reuse ~/.local/share/increading
        - [X] Functionality: use select Path for their extracts
        - The estructure should be like:
```
users-selected-path/
|--- extracts_from_book_1/
|    |--- extract-list-file.md
|    |--- individual-extract-file-1.md
|    |--- individual-extract-file-2.md
|--- extracts_from__book_2/
```

- [ ] Sqlite database

- [ ] Separate completely between code and interface, so it is easier to have
  multiple/modular interfaces
    - [ ] Create an interface class

- [ ] Add functionality to open files (materials) during session
    - [ ] Maybe a configuration menu at the beginning in which you can specify the programms to open different types of materials, even with the commands.
- [ ] Add functionality to add bookmark at the end
- [ ] Make independent extracts from "extract list" (_au contraire_: append new extracts to extract list)
    - [X] Markdown separated by "---" (the part in file manager is done)
- [ ] Add spaced repetition to extracts
- ...

## TODO: possible extra functionalities

- [ ] Possibility to change frequency to materials (for instance, lapses of 2 days)

- [ ] Possibility to simply go into the app to add a new extract (imagine you see something and open the app just to record it)
    - [ ] Add a new material and a new extract
    - [ ] Add a new extract to an existing material

- [ ] Be able to create different priority queues

- [ ] Exporting data and making backups

- [ ] Make Linux package 
- [ ] Make windows executable


## Known limitations

- When creating the "extracts directory", if the path selected needs to create a
parent directory, but a file exists with that name, it will broke. Don't have
the time to fix this error (in file_manager.py, `create_directory()`). 
    - Could be solved checking that every parent directory exists or is a
    directory. (Maybe chopping the path string, but there may be directories I
    can't access...)
    - Can also be solved with the user interface by forcing the user not to be a
    jerk.

- Problems with privileged directories?