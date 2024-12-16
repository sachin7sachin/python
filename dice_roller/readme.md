Overview
This Python program simulates rolling a specified number of dice and displays the result in an ASCII art representation. Each die is randomly rolled, and its result is shown in the form of dice faces, similar to how you would see them on a real die. The total of all dice rolls is also calculated and displayed.

Features
Random Dice Rolls: The program generates random numbers between 1 and 6, representing a dice roll.
ASCII Art Dice Faces: Each dice roll is displayed using ASCII art that visually represents the number rolled.
Total Calculation: After displaying the dice faces, the program calculates and prints the total sum of all dice rolls.
Customizable Number of Dice: The user can specify how many dice they want to roll.
How to Play
The program will prompt you to enter the number of dice to roll.
After you enter the number of dice, the program will simulate rolling each die and display their faces using ASCII art.
The program will then calculate and display the total sum of the rolled numbers.
Game Flow
The user is prompted to input the number of dice they want to roll.
For each die:
A random number between 1 and 6 is generated.
The dice face corresponding to the number is printed in a grid using ASCII art.
The total of all rolled dice is displayed.
The program ends after printing the dice faces and the total.
Technologies Used
Python 3.x
Random module for generating random numbers.
Code Explanation
Dice Faces: A dictionary dice_art is used to store the ASCII art for each dice face, corresponding to the numbers 1 through 6.
Random Dice Rolls: The program generates a random number for each dice using the random.randint(1,6) function.
Displaying Dice Faces: The program loops through each dice roll and prints the appropriate ASCII art for each dice side.
Total Calculation: After displaying the dice faces, the program calculates the sum of the rolled dice and prints it