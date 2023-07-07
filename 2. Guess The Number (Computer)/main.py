import random
# For importing a random number

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    # We're setting the value of guess as 0. So, it is never equal to the random number
    while (guess!= random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < random_number:
            print("Sorry, guess again. Too low.")

        elif guess > random_number:
            print("Sorry, guess again. Too high")
    
    print(f"Yay, congrats. You have guess the number {random_number} correctly!")

guess(100)
# So, it will be between 1 and 100.