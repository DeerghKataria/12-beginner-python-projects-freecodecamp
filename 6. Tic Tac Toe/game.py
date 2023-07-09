from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep 3 * 3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to which particular box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # moves = []
        # for(i, x) in enumerate(self.board):
        #     # ['x', 'x', 'o'] ----> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

        # Rather than typing the entire for loop. You can essentially write this one line.
        # This basically means that wherever there is a ' ' space. Fill it with 'i'
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    # To check for the empty squares
    def empty_sqaures(self):
        return ' ' in self.board
    
    # Also, for returning the number of empty sqaures
    def num_empty_sqaures(self):
        return len(self.available_moves())
    
    def make_move(self, sqaure, letter):
        # if valid move, then make the move (assign sqare to letter)
        # then return true. If invalid, return false.

        if self.board[sqaure] == ' ':
            self.board[sqaure] = letter
            if self.winner(sqaure, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere.... we have to check all these!
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check Diagnols
        # but only if the sqaure is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagnol.

        if square % 2 == 0:
            diagnol1 = [self.board[i] for i in [0, 4, 8]] #left to right diagnol
            if all([spot == letter for spot in diagnol1]):
                return True
            diagnol2 = [self.board[i] for i in [2, 4, 6]] #left to right diagnol
            if all([spot == letter for spot in diagnol2]):
                return True
            
        # if all of these fail
        return False

def play(game, x_player, o_player, print_game = True):
    # returns the winer of the game(the letter)! or None for a tie

    # The value is set to be true, because let's say in 
    # the future you want the computer to play against itself.
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # Starting Letter

    # Iterate while the game still has empty sqaures
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)

    while game.empty_sqaures():
        # get the move fro the appropriate player
        if letter == 'O':
            sqaure = o_player.get_move(game)
        else:
            sqaure = x_player.get_move(game)
        
        # Let's define a function to make a move!

        if game.make_move(sqaure, letter):
            if print_game:
                print(letter + f'makes a move to sqaure {sqaure}')
                game.print_board()
                print('')   # Just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # Switches Player
    
        # tiny break, to make things easier to read
        time.sleep(0.8)

    if print_game:
            print("It\'s a Tie!")
        
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)

