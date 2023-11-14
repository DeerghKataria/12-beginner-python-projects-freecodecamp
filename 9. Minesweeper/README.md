# Minesweeper Game

This Python script implements the classic Minesweeper game in the command line.

## Description

This implementation of Minesweeper allows players to enjoy the classic game on their console. Players can uncover cells on the board, and their goal is to clear the board without detonating any bombs.

## Features

- Dynamic board creation based on dimensions and number of bombs
- Player-friendly interface in the command line
- Recursive digging for empty cells
- Win or lose condition based on uncovering cells without hitting a bomb
- Detailed error handling for invalid inputs

## How to Play

1. **Run the Game:**
   - Execute the Python script `minesweeper.py`.
   
2. **Game Rules:**
   - You are presented with a board of hidden cells.
   - Enter the coordinates (row, col) to dig and uncover cells. (Example: `0,2`)
   - Avoid uncovering cells with bombs.
   - The game ends if a bomb is uncovered or when all non-bomb cells are revealed.

## Installation

Ensure you have Python installed. This script runs on Python 3.

## How to Run

```bash
python minesweeper.py
```

## Customization
You can modify the game's settings:

dim_size: Set the board's dimensions (default: 10x10)
num_bombs: Set the number of bombs on the board (default: 10)