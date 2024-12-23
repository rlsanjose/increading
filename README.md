# increading

A simple incremental reading app for the terminal.

## Description

This is a (very) simple implementation of some of the core ideas of
[Incremental Reading](https://supermemo.guru/wiki/Incremental_reading).

Although it may be functional, this version is in a _beta_ stage and
it may contain important errors. Use at your discretion. I'll try to
improve it.

Feel free to contribute with pull requests. Bellow there is a to-do
list with some ideas.

## Requirements

- Python 3 (currently tested with 3.12).
- Sqlite3.
- Vim.
- A Linux system that is "XDG Base Directory" compliant. In this case,
the app will use `~/.local/share/` for the user data (sqlite database)
and `~/.config/` for the config file.

## Installation

At the moment, there is no package or executable. You will need to
clone this repository and then run:

```shell
python3 src/main.py
```

## Usage

The program has two main elements: materials and extracts. _Materials_
are the content you consume (books, articles, videos, etc.).
_Extracts_ are quotes or ideas you write down from the materials.

In each session, you will review a series of materials and extracts.
The idea is to _extract_ extracts out of the materials, and then
_incrementally_ (throughtout multiple sessions) process the extracts
to convert them in anki cards and add them manually. When this is
done, you can mark the extract as _ended/suspended_. The extracts will
be showed in increasing intervals (first, between 1-3 days; then, each
interval will increase by 2.5x), unless you reset the schedule
(punctuate with 0 when reviewing). You also can _pospone_ materials
and extracts X days if you don't feel like reviewing them this moment.

The creation and edition of the extracts is (at the moment) hardcoded
to be done with _vim_. Change the code in `src/file_manager.py` if you
want other editor.

Every extract will have its own file (in `~/increading`). When
created, each file will be concatenated into a general file, which
will contain every original quotation you extracted.

## TODO:

- [ ] Refactor
- [ ] Testing
- [ ] Improve the user interface
- [ ] Option to customize material and extract frequency, a_factor...
- [ ] Make possible to later modify things like path, name, author, priority
- [ ] Show and manage the table of materials and extracts.
- [ ] Possibility to simply go into the app to add a new extract
(imagine you see something and open the app just to record it)
    - [ ] Add a new material and a new extract
    - [ ] Add a new extract to an existing material
- [ ] Delete an extract (for now, mark as suspended)
- [ ] Select the editor of preference for the extracts
- [ ] Open path in pdf viewer, or the browser...
- [ ] Anki connection of some kind
- [ ] Be able to create different priority queues
- [ ] Exporting data and making backups
- [ ] Address the rest of supermemo functionality
- [ ] Make Linux package 
- [ ] Make it OS agnostic
