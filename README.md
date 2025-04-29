# project8.py
# Translator Project

This is a simple python program that translates text between English and persian using a text file as a dictionary.

## Features
- Translate english to persian and persian to english using a local dictionary ('translate.txt').
- Add new words to the dictionary.
- A  menu-based interface to choose actions (translate, add word,exit).

## Requirements
To run the program, you need:
- Python 3.6 or higher.
- A 'translate.txt' file containing word pairs.

## Installation
1. Install python if you don't have it (version 3.6 or higher).
   - Download python from [python.org](https://www.python.org/downloads/) and follow the installation instructions.
   - Make sure to add python to your system PATH during installation.
2. No additional libraries are required since the program uses only standard python.

## Instructions
Follow these steps to set up and run the project:

1. **Clone the repository** (if you haven't already):
```bash
git clone https://github.com/yourusername/translator-project.git
cd translator-project
```
1. Create the Dictionary File:
   - create a file named <span style="color: red;"> translate.txt </span> in the project directory.
   - Add word pairs, one pair per line, in the format  <span style="color: red;">english_word persian_word. </span> Example:
```
hello salam
world jahan
```
2. Run the program:
   - Open a terminal in the project directory.
   - Run the script:
   ```
   python translate.py
   ```
3. Use the program:
   - The program will display a menu:
```
welcome to my translate
1- translate english to persian
2- translate persian to english
3- ass a new word to database
4- exit
```
- Enter a number (1-4) to choose an action:
  1. Enter an English  text (e.g., <span style="color: red;"> hello world </span>) to translate it to persian (e.g., <span style="color: red;"> salam jahan </span>).

  2. Enter a Persian text (e.g., <span style="color: red;"> سلام جهان </span>) to translate it to English (e.g., <span style="color: red;"> hello world </span>).

  3. Add a new word pair to the dictionary (e.g., <span style="color: red;"> good خوب </span>).

  4. Exit the program.

# File structure
 - <span style="color: red;"> translate.py </span>: The main script with the translation functionality.
 - <span style="color: red;"> translate.txt </span>: A text file containing word pairs for translation (e.g., <span style="color: red;"> hello salam </span>).

# Example Usage
1. Run the program.
2. Choose option 1 (Translate English to Persian).
3. Enter: <span style="color: red;"> hello world </span>
4. Output: <span style="color: red;"> salam jahan </span>

# Notes
- If <span style="color: red;"> translate.txt </span>is not found, the program will display a message asking you to create it.
- If a word is not the dictionary, it will remain unchanged in the output.
- The program currently translates word, not full sentences.

# Future Improvements
- Add an API(e.g., google Translate) to translate full sentences.
- Create a graphical user interface (GUI)
- Add unit tests to validate the translation functions.

# Author
Created by Yousef as part of Assignment 8 for a python programming course.
