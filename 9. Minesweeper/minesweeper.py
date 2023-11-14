import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size        # For the dimension size
        self.num_bombs = num_bombs      # For the number of bombs

        # For creating a board
        # Helper Function
        self.board = self.make_new_board()  # Plant the bombs
        self.assign_values_to_board()

        # For initializing the st of uncovered locations
        # We'll save the (row, col) tuples into this set
        self.dug = set()    # If we dig at 0, 0. Then self.dug = {(0,0)}

    def make_new_board(self):
        # It is going to construct a board based on the dimension size.
        # We will construct the list of lists here since it's best for 2D game.

        # For generating a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # This would create an array that looks like this:
        # [[None, None, ..... None],
        # [None, None, ..... None],
        # [None, None, ..... None],
        # [None, None, ..... None],
        # [None, None, ..... None],
        # [None, None, ..... None]]
        # We can see how this represents a board!

        # For planting the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size*2 - 1)    # It would return a random integer N such that a <= N <= b.
            row = loc // self.dim_size  # We want the number of times dim_size goes into loc to tell us about the row.
            col = loc % self.dim_size   # We want the remainder to tell us what in that row to locate

            if board[row][col] == '*':      # This '*' is used to indicate the  bomb
                # This means that we have already planted a bomb there.
                continue

            board[row][col] = '*'   # Plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # Now that we have the bombs planted, let's assign a number for all the bombs planted
        # represents how many neighbouring bombs there are, we can precompute these and it'll save us some
        # effort checking what's around the board later on.

        for r in range(self.dim_size):          # Row Index
            for c in range(self.dim_size):      # Column Index
                if self.board[r][c] == '*':
                    # If this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)

    def get_num_neighbouring_bombs(self, row, col):
        # Let's iterate through eac of the neighbouring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # Make sure to not go out of bounds!

        num_neighbouring_bombs = 0
        for r in range(max(0, row-1) , min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col-1)+1):
                if r == row and c == col:
                    # our original location, dont' check
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
        
        return num_neighbouring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at a location with neighbouring bombs -> finish dig
        # dig at location with no neighbouring bombs -> recursively dig neighbours!

        self.dug.add((row, col))    # Keeping track that we dug here or not

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row-1) , min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col-1)+1):
                if (r, c) in self.dug:
                    continue    # don't dig where you've already dug
                self.dig(r, c)

        # If our initial dig didn't hit a bomb, we shouldn't hit a bomb here
        return True

    def __str__(self):
        # This is a magic function where if you call print on this object.
        # It will print out what this function returns!
        # Return a string that shows the board to the player

        # First let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if(row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else: 
                    visible_board[row][col] = ' '   # Because the user shouldn't be able to see what's at that location yet
        
        # For putting this entire thing togoether in a string
        
        
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# Play the game

def play(dim_size = 10, num_bombs=10):
    # Step 1: Create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: Show the user the board and ask for where they want to dig
    # Step 3a: If location is a bomb, then show that the game is over
    # Step 3b: If location is not a bomb, dig recursively unti leach square is at
    # least next to a bomb
    # Step 4: Repeat steps 2 and 3. Until there are no places to dig, which leads
    # to victory.

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # We're using "re" to even input something like this 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhh
            break # (game over rip)

    # 2 ways to end loop, lets check which one
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        # let's reveal the whole board!
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # good practice :)
    play()



