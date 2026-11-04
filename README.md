# MYSTERY ISLAND: THE LOST LIGHTHOUSE

## Project Overview

Mystery Island: The Lost Lighthouse is a text-based adventure game developed with Python.

The player is stranded on a mysterious island after a terrible storm. The mission is to explore different locations, collect useful objects, make important decisions, discover clues and restore the lighthouse to win the game.

## Features

- Interactive text-based gameplay.
- Five connected locations.
- Player energy management.
- Item collection and inventory tracking.
- Meaningful decisions with consequences.
- Puzzle clues and a final lighthouse challenge.
- Movement restrictions based on collected items.
- Input validation and error handling.
- Winning, losing and replay options.
- Automated unit tests.

## Project Structure

```text
mystery_island/
├── main.py
├── game.py
├── README.md
├── .gitignore
└── tests/
    └── test_game.py
```

## Requirements

- Python 3.10 or later.
- No external Python packages are required.

## How to Run

1. Clone or download the project.
2. Open the project directory in your terminal.
3. Run:

```bash
python3 main.py
```

## Game Locations

The island contains five locations:

1. Beach
2. Jungle
3. Cave
4. Old Bridge
5. Lighthouse

## Game Rules

- The player starts with 5 energy points.
- Moving between connected locations costs 1 energy point.
- The Rope is required to cross the Old Bridge.
- The Lantern is required to enter and light the Lighthouse.
- Certain decisions reveal useful clues.
- Taking the longer route in the Jungle costs energy.
- An incorrect lighthouse answer costs energy.
- The player wins by entering the correct lighthouse sequence.
- The player loses when energy reaches zero.

## Controls

The game uses a numbered menu:

1. Collect available item.
2. Move to another location.
3. Explore location.
4. View inventory.
5. View player status.
6. Quit game.

When moving, players can select a destination using its number or name.

## Running the Tests

From the project root, run:

```bash
python3 -m unittest discover -s tests -v
```

The tests verify game initialization, item collection, movement, decisions, energy management, puzzle solving and the complete winning journey.

## Technologies

- Python
- Python unittest

## Project Purpose

This project demonstrates practical Python programming concepts, including functions, dictionaries, lists, conditional statements, loops, input validation, modular programming and automated testing.
