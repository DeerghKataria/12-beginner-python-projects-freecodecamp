def find_next_empty(puzzle):
    # Finds the next row, col on the puzzle that's not filled yet ---> replace it with -1
    # return row, col tuple (or (None, None) if there is none)

    # Our indices are marked from 0-8

    for r in range(9):
        for c in range(9):  # range(9) is 0, 1, 2, 3... till 8
            if puzzle[r][c] == -1:
                return r, c
    return None, None   # This means that there are no spaces in the puzzle leftk

def is_valid(puzzle, guess, row, col):
    # Figures out whether the guess at that row/col is a valid guess or not?
    # returns True if is valid, False otherwise

    # Let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # Now the columns
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # and then for square you have to iterate over the 3x3 values in the row/col

    row_start = (row // 3)  # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3)

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # If we get here, these checks pass
    return True
    
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
    for guess in range(1, 10):   # 1, 2, 3.....9
        # Step 3: To check whether this is a valid guess or not
        if is_valid(puzzle, guess, row, col):

    