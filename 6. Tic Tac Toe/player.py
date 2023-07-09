import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # We want all players to get their next move given a game
    def get_move(self, game):
        pass

# This is for the Computer Player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

# This is for Human Player
class HumanPlayer(Player): 
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8):")
            # We're going to check that this ia correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid
            # if that spot is not available on the board, we also say its invalid.

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!

            except ValueError:
                print("Invalid sqaure. Try again!")
                
        return val  # So, this going to be the human player's next move.
