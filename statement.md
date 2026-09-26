## Project Statement

# Project Title
Word Scramble Challenge – A Python Command-Line Game

# Problem Statement
* This project aims at creating a simple Word Scramble Game which is based on the use of Python.
* The computer chooses a word at random from a pre-determined list of words and then rearranges the letters of that word.
* The player has to recognise and input the original word
* The game offers various difficulty levels so that the player can select words appropriate to their level.
* For each word the player is given three attempts
* A correct guess causes the player's score to go up by one, and if the player is not able to work out the word within the available attempts then the correct answer is shown.

# The extent of the project
* The project consists of a command-line interface and includes features such as word selection, word scrambling, taking user input, checking the answers, managing the attempts, scoring and selecting the difficulty level before allowing a replay.
* The project is not based on a database or any external packages.

# Target Users
* Students who are learning basic Python programming.
* People who are just starting out and would like to practice programming by playing a small game.
* People who would like a simple word-based command-line game.

# Objectives
The project is designed to practise:
* Variables and data types
* Lists and dictionaries
* Strings and string operations
* User input using input()
* if-elif-else statements
* for and while loops

# Functions
* The random module
* Basic program logic and problem solving
* Multiple Python files and modular organization
* Easy, Medium and Hard difficulty levels
* 5 random words per game
* 3 attempts for each word
* Automatic answer checking
* Score out of 5
* Cumulative score for multiple games
* Replay option
* Input validation
* Modular project structure
* Basic validation tests

# Functional Modules
* Word Management: The file word_bank.py contains the word lists for the Easy, Medium and Hard levels.
* Game Logic: The program game_logic.py chooses five random words, scrambles them, handles the attempts, checks the answers and computes the score.
* User Interaction: The files utils.py and input_handler.py show the menus and obtain validated user input.
* Score Management: The program score_manager.py shows the score for a game as well as the final total result.

# Non-Functional Requirements
* Usability features a simple and clear interaction through the command line.
* Performance includes quick selection of words and checking of answers.
* Reliability is ensured by validating invalid menu inputs.
* The functions are spread out among relevant files.
* The game makes use of short word lists that are kept in memory.
* It is portable since it makes use of functionality from the Python standard library.

# How the Programme Works
* Display the welcome message.
* Request that the player choose a difficulty level.
* Choose 5 words at random from those at the selected difficulty level.
* Rewrite the letters in every word.
* Display the scrambled word.
* The player should be given 3 tries to guess the word.
* The score should be increased when the answer is correct.
* Show the score after the five words have been displayed.
* Inquire if the player would like to play again.
* When the player leaves, show the cumulative result.

# Technology Used
* Programming Language: Python 3
* Module Used: random
* Interface: Command Line Interface (CLI)

Version Control: Git and GitHub
