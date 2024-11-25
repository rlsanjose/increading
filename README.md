# increading

A simple CLI incremental reading app.

## TODO

- [X] Add type to Materials (pdf, web, epub...)
- [X] Add extract list to materials (has to be another object)
- [X] Replace loops with min function. Better: use sort function
- [X] Add functionality to add extracts during session
    - [X] For now, I can hard-code it to work with vim (look later vim
    sessions...). Later, we will let the user decide.

- [ ] Create path variables for extract_list and extract
    - [ ] Functionality: use select Path for their extracts
    - The estructure should be like:
```
users-selected-path/
|--- extract_name_1/
|    |--- extract-list-file.md
|    |--- individual-extracts/
|         |---individual-extract-file-1.md
|         |---individual-extract-file-2.md
|--- extract_name_2/
```

- [ ] Add functionality to open files (materials) during session
    - [ ] Maybe a configuration menu at the beginning in which you can specify the programms to open different types of materials, even with the commands.
- [ ] Add functionality to add bookmark at the end
- [ ] Make independent extracts from "extract list"
    - [ ] Markdown separated by "---"
- [ ] Add extract spaced repetition
- ...
- [ ] Possibility to change frequency to materials (for instance, lapses of 2 days)


- [ ] Create objects
    - [X] Materials
    - [ ] Extracts
    - [ ] Priority Queue
        - [ ] Have different priority queues
    - [ ] Daily Queue

- [ ] Sqlite database

- [ ] Exporting data and making backups

- [ ] Separate completely between code and interface, so it is easier to have
  multiple/modular interfaces
    - I'm thinking about it as the next: the interface should be on its own class or module. The functions should be well specified. It should be as easy as calling those functions from an external module to control this things.

- [ ] Make Linux package 
- [ ] Make windows executable