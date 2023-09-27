# AI Tic Tac Toe with Minimax Algorithm

This is a Python implementation of the classic Tic Tac Toe game, where you can play against an AI opponent that uses the Minimax algorithm to make decisions. The game allows you to choose your opponent, either a random computer player or a genius computer player that employs the Minimax algorithm for optimal moves.

## Table of Contents

- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Customizing the AI](#customizing-the-ai)
- [License](#license)

## Getting Started

To get started, you'll need to have Python 3 installed on your computer.

1. Clone this repository:

2. Navigate to the project directory:

3. Run the game:


## How to Play

1. Choose 'X' or 'O' to start the game.
2. Enter your move by specifying a number from 0 to 8 (corresponding to the board positions).
3. The AI opponent (GeniusComputerPlayer) will make its move using the Minimax algorithm.
4. Continue taking turns until one player wins or the game ends in a tie.

## Code Structure

The project consists of two Python files:

- `game.py`: Contains the main game logic, including the TicTacToe class and the `play` function to run the game.
- `player.py`: Defines the player classes, including `HumanPlayer`, `RandomComputerPlayer`, and `GeniusComputerPlayer`.

### `game.py`

- `TicTacToe`: Represents the game board and logic.
- `print_board`: Prints the current game board.
- `print_board_nums`: Prints the board with numbered positions for reference.
- `available_moves`: Returns a list of available moves (empty squares).
- `make_move`: Attempts to make a move on the board.
- `winner`: Checks if a player has won.
- `play`: Runs the game and allows players to take turns.

### `player.py`

- `Player`: Base class for all players.
- `RandomComputerPlayer`: A computer player that makes random moves.
- `HumanPlayer`: Represents a human player.
- `GeniusComputerPlayer`: A computer player that uses the Minimax algorithm for intelligent moves.

## Customizing the AI

You can customize the AI player by modifying the `GeniusComputerPlayer` class in `player.py`. Adjust the logic inside the `minimax` method to fine-tune the AI's decision-making process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
