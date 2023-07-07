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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high because low = high

        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)?").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'\nYay, the computer guessed the number, {guess} ,correctly!')

computer_guess(100)
# So, it will be between 1 and 100.