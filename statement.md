# Project Statement

## 1. Project Title

**Word Scramble Challenge – A Python Command-Line Game**

## 2. Problem Statement

The objective of this project is to develop a simple command-line based **Word Scramble Game using Python**.

The computer selects a word randomly from a predefined word bank and rearranges its letters. The player has to identify and enter the original word. The game provides different difficulty levels so that the player can choose words according to their level.

The player gets **3 attempts for each word**. A correct answer increases the player's score by one. If the player is unable to guess the word within the given attempts, the correct answer is displayed.

## 3. Scope of the Project

The project is limited to a command-line interface. It includes word selection, word scrambling, user input, answer checking, attempt management, scoring, difficulty selection and replay.

The project does not use a database or external packages.

## 4. Target Users

- Students learning basic Python programming.
- Beginners who want to practise programming through a small game.
- Users who want a simple word-based command-line game.

## 5. Objectives

The project is designed to practise:

- Variables and data types
- Lists and dictionaries
- Strings and string operations
- User input using `input()`
- `if-elif-else` statements
- `for` and `while` loops
- Functions
- The `random` module
- Basic program logic and problem solving
- Multiple Python files and modular organization

## 6. High-Level Features

- Easy, Medium and Hard difficulty levels
- 5 random words per game
- 3 attempts for each word
- Automatic answer checking
- Score out of 5
- Cumulative score for multiple games
- Replay option
- Input validation
- Modular project structure
- Basic validation tests

## 7. Functional Modules

### Word Management
`word_bank.py` stores the word lists for Easy, Medium and Hard levels.

### Game Logic
`game_logic.py` selects five random words, scrambles them, manages attempts, checks answers and calculates the score.

### User Interaction
`utils.py` and `input_handler.py` display menus and receive validated user input.

### Score Management
`score_manager.py` displays the score for a game and the final cumulative result.

## 8. Non-Functional Requirements

- **Usability:** simple and clear command-line interaction.
- **Performance:** quick word selection and answer checking.
- **Reliability:** invalid menu inputs are handled through validation.
- **Maintainability:** functions are divided across meaningful files.
- **Resource Efficiency:** the game uses small in-memory word lists.
- **Portability:** it uses Python standard-library functionality.

## 9. Working of the Program

1. Display the welcome message.
2. Ask the player to select a difficulty level.
3. Select 5 random words from the selected difficulty.
4. Scramble the letters of each word.
5. Display the scrambled word.
6. Allow the player 3 attempts to guess the word.
7. Increase the score when the answer is correct.
8. Display the score after all 5 words.
9. Ask whether the player wants to play again.
10. Display the cumulative result when the player exits.

## 10. Technology Used

**Programming Language:** Python 3

**Module Used:** `random`

**Interface:** Command Line Interface (CLI)

**Version Control:** Git and GitHub
