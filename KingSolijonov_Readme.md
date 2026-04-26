# Cluedo Game - Project 2 Part 1

## Student Name
King Solijonov

## Project Description
This project is a text-based Python implementation of Part 1 of a digital Cluedo/Clue game. The game allows the player to explore a mansion, move between connected rooms, and make murder suggestions involving a character, weapon, and room.

## Features Implemented

### Game Setup
- Mansion layout with multiple rooms:
  - Kitchen
  - Ballroom
  - Conservatory
  - Dining Room
  - Lounge
  - Hall
  - Study
  - Library
  - Billiard Room
- Character definitions with starting positions:
  - Miss Scarlett
  - Colonel Mustard
  - Mrs. White
  - Mr. Green
  - Mrs. Peacock
  - Professor Plum
- Weapon definitions:
  - Candlestick
  - Revolver
  - Rope
  - Lead Pipe
  - Knife
  - Wrench
- Random solution selection:
  - One character
  - One weapon
  - One room

### Player Movement
- Players can move between connected mansion rooms.
- Players can view their current location and available room connections.

### Suggestions
- Players can make suggestions after entering a room.
- Each suggestion includes:
  - A character
  - A weapon
  - The current room
- The game provides feedback showing how many parts of the suggestion match the hidden solution.

## Files Included
- `cluedo_game.py` - Main Python source code file.
- `KingSolijonov_Readme.md` - Instructions and project documentation.

## Dependencies / Prerequisites
This project only requires Python.

Recommended version:
- Python 3.10 or higher

No external libraries are required.

## How to Run the Game

### Option 1: Run Locally

1. Download or unzip the project folder.

2. Open a terminal or command prompt.

3. Navigate to the source code directory:

```bash
cd KingSolijonov_Project2_SourceCode
```

4. Run the game:

```bash
python cluedo_game.py
```

or, depending on your system:

```bash
python3 cluedo_game.py
```

## How to Play
1. Start the game.
2. Choose a character.
3. View your current room and connected rooms.
4. Move between rooms.
5. Make suggestions using a character, weapon, and your current room.
6. Use the feedback to reason about the hidden murder solution.
7. Quit when finished.

## Notes
This version is designed for Project 2 Part 1. It focuses on:
- Game setup
- Mansion layout
- Character and weapon definitions
- Random solution generation
- Movement
- Suggestions

Future versions could include:
- Multiple players
- Cards and clue distribution
- Accusations
- Win/loss conditions
- More advanced AI reasoning
