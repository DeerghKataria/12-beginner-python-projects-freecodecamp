import random
import string

from words import words

# Since, some words have spaces and dashes between them. So, we don't want that
# in our Hangman game. So, we will discard such words

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # What the user has guessed

    # Introducing the concept of lives
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Letters they have already used
        # ' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))

        # What current word is (i.e. W - R D )
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # Getting User Input
        user_letter = input("\nGuess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1   # Take away a life if wrong
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again!")

        else:
            print("You typed a invalid character.")

    # It gets here where len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f"\nYou died. Sorry the word was {word}!!!")
    else:
        print(f'\nYou guessed the word - {word}!!!')

hangman()
