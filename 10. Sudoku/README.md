# Sudoku Solver
A Python script (sudoku.py) for solving Sudoku puzzles using the backtracking algorithm. The script provides functions to check the validity of a Sudoku puzzle, find empty spaces, and solve the puzzle recursively.

# Functions
`find_next_empty(puzzle)`
Finds the next empty cell (represented by -1) in the Sudoku puzzle.

Returns: (row, col) tuple if an empty cell exists, (None, None) otherwise.
`is_valid(puzzle, guess, row, col)`
Checks if a guess is valid for the given row, column, and 3x3 square in the puzzle.

Returns: True if the guess is valid, False otherwise.
`solve_sudoku(puzzle)`
Solves the Sudoku puzzle using backtracking.

Mutates the input puzzle to the solution if it exists.
Returns: True if a solution is found, False otherwise.

Example
```
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    # Solve the Sudoku puzzle
    if solve_sudoku(example_board):
        pprint(example_board)
    else:
        print("No solution exists for the given Sudoku puzzle.")
```

# Usage
Clone the repository or copy the sudoku.py script into your project.
Use the provided functions to solve Sudoku puzzles in your Python project.
Feel free to customize the example puzzle or integrate the script into your applications. Enjoy solving Sudoku puzzles with Python!