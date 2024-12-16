
import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number,highest_number)
guesses = 0

print("------- Welcome to Number guessing game -------")
print(f"Select a number from the range {lowest_number}, {highest_number}")


while True:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess<answer:
            print("Too low! Try again")
        elif guess>answer:
            print("Too High! Try again")
        elif guess<lowest_number or guess > highest_number:
            print("The guess is out of range")
            print(f"please select a number from the range {lowest_number}, {highest_number}")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Your total number of guesses: {guesses}")
            break

    else:
        print("Invalid input")
        print(f"please select a number from the range {lowest_number}, {highest_number}")
