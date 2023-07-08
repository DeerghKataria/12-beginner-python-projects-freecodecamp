# Guess the Number Game
This is a simple number guessing game implemented in Python. The game allows you to either guess a randomly generated number or have the computer guess your number.

# How to Play
- Ensure you have Python installed on your machine.
- Clone or download the repository to your local machine.
- Open the command prompt or terminal and navigate to the project directory.
- Run the guess_number.py file using the command python guess_number.py.
- Follow the on-screen instructions to play the game.

# Features
1. Guessing a Number: In this mode, the computer generates a random number between a specified range, and you need to guess the number. The program will provide feedback on whether your guess is too high or too low until you guess the correct number.

2. Computer Guess: In this mode, you think of a number between a specified range, and the computer will try to guess your number. You need to provide feedback to the computer (whether its guess is too high, too low, or correct), and the computer will adjust its guess accordingly until it guesses your number correctly.

# Usage
- The guess_number.py file contains two functions: guess(x) and computer_guess(x), where x represents the upper limit of the number range. You can modify the value of x to change the range of numbers in the game.

- To play the game with your own guesses, call the guess(x) function and pass the upper limit as an argument. For example, to play with a number range from 1 to 100, use guess(100).

- To play the game with the computer guessing your number, call the computer_guess(x) function and pass the upper limit as an argument. For example, to have the computer guess a number between 1 and 100, use computer_guess(100).

# License
- This project is licensed under the MIT License. Feel free to modify and distribute it as per your needs.

# Contributing
- Pull requests are welcome. For major changes or enhancements, please open an issue first to discuss what you would like to change.

# Acknowledgments
- The game logic and structure of this project were inspired by Python programming tutorials and exercises.
- This project was developed for educational purposes as a demonstration of basic Python programming concepts.
- Feel free to customize and expand this README.md file as needed, adding any additional information or instructions that you find relevant to your game.