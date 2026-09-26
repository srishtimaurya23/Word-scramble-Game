# Word Scramble Challenge

A simple **command-line Word Scramble Game** made with Python as a VITyarthi project.

## Overview

The game selects five random words from a chosen difficulty level and scrambles their letters. The player gets three attempts for each word. A correct answer gives one point. The score is displayed after each game, and the cumulative score is displayed when the player exits.

## Features

- Easy, Medium and Hard levels
- 5 random words per game
- 3 attempts for each word
- Automatic answer checking
- Score out of 5 for each game
- Cumulative score for multiple games
- Input validation for difficulty and replay choices
- Modular Python files
- Basic validation tests

## Functional Modules

1. **Word Management** – `word_bank.py` stores words for each difficulty.
2. **Game Logic** – `game_logic.py` controls word selection, attempts, answer checking and scoring.
3. **User Interaction** – `utils.py` and `input_handler.py` handle menus and user input.
4. **Score Management** – `score_manager.py` displays game and final results.

## Non-Functional Requirements

- **Usability:** simple CLI prompts make the game easy to use.
- **Performance:** words are stored in memory and processed quickly.
- **Reliability:** invalid menu and replay choices are handled through validation.
- **Maintainability:** related functions are separated into modules.
- **Resource Efficiency:** only Python standard-library features are used.
- **Portability:** the program can run with Python 3.x.

## Requirements

- Python 3.x
- VS Code or any Python-supported editor
- Git for GitHub submission

**No external packages are required.**

## Project Structure

```text
Word-Scramble-Game/
├── main.py
├── game_logic.py
├── utils.py
├── input_handler.py
├── score_manager.py
├── word_bank.py
├── test_game.py
├── statement.md
├── README.md
├── PROJECT_REPORT.md
├── docs/
│   └── design.md
└── .gitignore
```

## Setup & Run

Clone the repository:

```bash
git clone https://github.com/srishtimaurya23/Word_scramble_Game.git
cd Word_scramble_Game
```

Run the game:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## How to Play

1. Select a difficulty level.
2. A scrambled word is displayed.
3. Enter your answer.
4. You get 3 attempts for each word.
5. Five words are played in one game.
6. Check your score.
7. Choose whether to play again.

## Testing

Run:

```bash
python test_game.py
```

The tests check:
- scrambled words contain the same letters as the original word
- all three difficulty levels exist
- every level has at least five words
- replay validation accepts only `y` or `n`

## Design Diagrams

The following design diagrams are available in [`docs/design.md`](docs/design.md):

- System Architecture Diagram
- Workflow Diagram
- Use Case Diagram
- Sequence Diagram
- Component/File Relationship Diagram

A database is not used in this project, so an ER diagram is not applicable.

## Project Report

A report draft covering the VITyarthi requirements is available in [`PROJECT_REPORT.md`](PROJECT_REPORT.md). The final report can be exported to PDF for portal submission.

## Screenshots

The following screenshots show the project running at different difficulty levels and results.

### Difficulty levels
<img width="460" height="252" alt="Difficulty levels" src="https://github.com/user-attachments/assets/3edeaabf-2b26-4703-967d-fe096bdb7f11" />

### Easy level
<img width="467" height="839" alt="Easy level" src="https://github.com/user-attachments/assets/f4ff2143-97d6-4385-a2b8-ae67b44dba50" />

### Easy result
<img width="468" height="404" alt="Easy result" src="https://github.com/user-attachments/assets/116ec6f8-45df-4976-914a-54aa5bdaf8b6" />

### Medium level
<img width="459" height="807" alt="Medium level" src="https://github.com/user-attachments/assets/40879ded-80a4-467f-95f8-d4f5cce2f5b2" />

### Medium result
<img width="466" height="396" alt="Medium result" src="https://github.com/user-attachments/assets/08bd36e5-aad4-4c0d-ad6e-4b88281c348d" />

### Hard level
<img width="468" height="867" alt="Screenshot 2026-09-22 000138" src="https://github.com/user-attachments/assets/6a02e00b-1175-4fa0-9443-092e126dd9ec" />

### Hard level continuation
<img width="458" height="110" alt="Hard level continuation" src="https://github.com/user-attachments/assets/69fbca47-0f16-4435-bbc8-6d8a56b84b34" />

### Hard result
<img width="461" height="321" alt="Screenshot 2026-09-22 000255" src="https://github.com/user-attachments/assets/b4ab2546-555f-47b2-9af2-c1ef99720b01" />


### Final result
<img width="451" height="68" alt="Final result" src="https://github.com/user-attachments/assets/56a3d38e-8153-4154-b564-e7075801e985" />

## Technologies

- Python 3
- `random` module
- Command Line Interface
- Git & GitHub

## Author

- **Name:** Srishti Maurya
- **Registration Number:** 26BAI10551
