Overview:

The "Number Guessing Game" is a simple interactive Python program where the player has to guess a randomly generated number within a specified range. The game provides feedback on whether the guess is too high, too low, or correct. It continues until the player guesses the correct number, counting the number of guesses made.

Features:

- Random Number Generation: A random number is chosen between 1 and 100.
- User Input: The user guesses a number by entering a value in the console.
- Feedback Mechanism: After each guess, the game provides feedback:
                      If the guess is too low or too high.
                      If the guess is outside the valid range (1 to 100).
                      If the guess is correct, it ends the game and shows the total number of guesses made.
- Input Validation: Ensures that the input is a valid number within the range, and prompts the user again if the
                    input is invalid
How to Play:

- The game will ask you to guess a number between 1 and 100.
- Enter a number and the game will tell you if your guess is too high, too low, or correct.
- If the guess is out of range or invalid, the game will prompt you to enter a valid number.
- The game continues until the correct number is guessed, and it will display the total number of guesses made.

Game Flow:

- The game will first ask the user to input a guess.
If the guess is:

- Too low, it will prompt the user to guess again with a higher number.
- Too high, it will prompt the user to guess again with a lower number.
- Correct, the game ends, displaying the number of guesses taken.
- If the input is invalid or out of range, it will display an error message and prompt the user to try again.

Technologies Used:

- Python 3.x
- Random module for generating the random number.

Code Explanation:

- Random Number Generation: A number between 1 and 100 is randomly selected using the random.randint() function.
- Guessing Loop: A while loop is used to allow repeated guesses until the correct number is guessed.
- Input Validation: The program checks if the user input is a valid number and within the specified range. If not,
                    it prompts for a valid input. 