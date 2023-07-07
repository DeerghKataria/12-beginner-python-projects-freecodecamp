# Number Guessing Game
This is a simple number guessing game implemented in Python. The program generates a random number between a specified range, and the player's task is to guess that number correctly.

# How to Play
Run the Python script guessing_game.py.
The program will prompt you to enter a number between 1 and a specified maximum value (x).
Enter your guess and press Enter.
Based on your guess, the program will provide feedback, telling you if your guess was too low or too high.
Keep guessing until you correctly guess the random number.
Once you guess the number correctly, the program will display a congratulatory message.

# Code Explanation
The game is implemented using the following steps:

The random module is imported to generate a random number.
The guess function is defined, which takes a parameter x representing the maximum value for the random number range.
Inside the function, a random number is generated using random.randint(1, x).
A variable called guess is initialized with 0.
A while loop is used to repeatedly prompt the player for guesses until the correct number is guessed.
Inside the loop, the player is prompted to enter a number between 1 and x.
The entered guess is compared with the random number.
If the guess is lower than the random number, a message is printed indicating that the guess was too low.
If the guess is higher than the random number, a message is printed indicating that the guess was too high.
When the guess matches the random number, a congratulatory message is displayed, and the loop terminates.
Finally, the guess function is called with a maximum value of 100 to start the game.
Feel free to modify the code and experiment with different ranges to enhance the game.

Have fun playing!