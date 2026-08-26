"""
- Garrison Moore
Simpuhl Dice roller
"""

#INTRODUCTION - asks the user for varibales for the amount of sides the die should have and how many rounds to play.

# *** USING OFFICIAL ASCII COLORS CODE - https://pypi.org/project/ascii-colors/
from ascii_colors import ASCIIColors, rich

# import randint
from random import randint 

# import os
import os

# import time
import time

print ("\n")

# MAIN STRING VOID ARGS

# Panels for highlighting content
ASCIIColors.panel("⚂ DICE ROLLER ⚀", title="Welcome to", border_style="green")

# Get user input for the number of sides on the die and store in a variable
user_input_1 = input("How many sides should your dice have?")

# type cast the user input to a integer for use later
sides_of_die = int(user_input_1)

# Confirm user selection
print(f"OK, your dice will have {user_input_1} sides\n")

# Get user input for the amount of rounds to play and store in a variable
user_input_2 = input("How many rounds do you want to play?")

# type cast user input to an integer
rounds = int(user_input_2)

# confirm user selection
print(f"OK, we will play {rounds} number of rounds.\n")


# GAME LOGIC - A for loop that runs for user specified # of rounds with user specified # of sides on each dice.
# Adds scores and prints total score at the end

# creating a list to track scores
score = []

# Creating a variable to track iterations
iteration = 0

# for loop runs for user specified # of rounds
for i in range (rounds) :

    # random number generator that uses user defined variable
    random_number_generator = randint(1, sides_of_die)

    # print the random number (Superceded by ASCIIColores.table)
    # print(random_number_generator)

    # append each dice roll to the list of scores
    score.append(random_number_generator)

    # add 1 to iteration count at the end of loop
    iteration += 1

    # Test code to clear screen (provided by Gemini Pro)
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCIIColor Table that refreshes for each round
    ASCIIColors.table(
        "[yellow]Iteration[/yellow]", "[yellow]Score[/yellow]",
        rows=[
            [iteration, score],
        ],
        title=("Score Sheet"),
        border_style="green"
    )

    # short pause for readability
    time.sleep(0.5)

# DEBUG iteration print
print(f"\n**DEBUG** iterations gone through - {iteration}\n")

# create a final score vriable that sums all values in the score list 
final_score = sum(score)

# ASCIIColor Table for final score display
ASCIIColors.table(
    "[green]Total rolls[/green]", "[green]Final Score[/green]",
    rows=[
        [iteration, final_score],
    ],
    title=("[yellow]FINAL SCORES[/yellow]"),
    border_style="Yellow"
)

# Print final score (superceded by ASCIIColors table)
#print(f"Final score : {final_score}")