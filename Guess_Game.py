import random

winning_no = random.randint(1, 10)
guess = 1
while True:
    guess_no = int(input("Guess: "))
    if guess_no == winning_no:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess_no < winning_no:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess += 1
