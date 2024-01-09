def find_next_empty(puzzle):
    # Finds the next row, col on the puzzle that's not filled yet ---> replace it with -1
    # return row, col tuple (or (None, None) if there is none)

    # Our indices are marked from 0-8

    for r in range(9):
        for c in range(9):  # range(9) is 0, 1, 2, 3... till 8
            if puzzle[r][c] == -1:
                return r, c
    return None, None   # This means that there are no spaces in the puzzle leftk

def solve_sudoku(puzzle):
    # We will be solving sudoku using backtracking
    # We will be using a list of lists since lists are mutable (i.e. they can be changed later)
    # Returning a solution
    # Mutates puzzle to the solution if the solution exists.

    # Step 1: Choosing a position of the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: This is a validation check to see whether we're left with valid inputs or not
    if row is None:
        return True
    
    # Step 2: If there is a place to put a number, then we can make a guess between 1 and 9
    for guess in range(1, 10)   # 1, 2, 3.....9
        # Step 3: To check whether this is a valid guess or not 