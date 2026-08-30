"""
- Garrison Moore
Simpuhl Dice roller
"""

# *** USING OFFICIAL ASCII COLORS CODE - https://pypi.org/project/ascii-colors/
from ascii_colors import ASCIIColors, rich
from random import randint
import os
import subprocess
import time

reset = True

while reset:
    # INTRODUCTION - asks the user for varibales for the amount of sides the die should have and how many rounds to play.

    # clear terminal
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    # line space for readability
    print ("\n")

    # Welcome panel
    ASCIIColors.panel("⚂ DICE ROLLER ⚀", title="Welcome to", border_style="green")

    # Use an if statement inside a while loop to ensure user input is numeric
    while True:
        # Get user input for the number of sides on the die and store in a variable
        user_input_1 = input("How many sides should your dice have?")

        # if user input is numeric, break out of loop
        if user_input_1.isnumeric():
            break
        else:
            # else keep running the loop
            print("Please enter a number")
            continue

    # type cast the user input to a integer for use later
    sides_of_die = int(user_input_1)

    # Confirm user selection
    print(f"OK, your dice will have {user_input_1} sides\n")

    # using the same loop structure from above to ensure user input is numeric
    while True:
        # Get user input for the amount of rounds to play and store in a variable
        user_input_2 = input("How many times do you want to roll the dice?")
        if user_input_2.isnumeric():
            break
        else:
            print("Please enter a number")
            continue

    # type cast user input to an integer
    rolls = int(user_input_2)

    # confirm user selection
    print(f"OK, we will roll {rolls} of your dice.\n")
    time.sleep(2)

    # GAME LOGIC - A for loop that runs for user specified # of rounds with user specified # of sides on each dice.
    # Adds scores and prints total score at the end

    # creating a list to track scores
    score = []

    # Creating a variable to track iterations
    iteration = 0

    # for loop runs for user specified # of rolls
    for i in range (rolls) :

        # random number generator that uses user defined variable
        random_number_generator = randint(1, sides_of_die)

        # print the random number (Superceded by ASCIIColores.table)
        # print(random_number_generator)

        # append each dice roll to the list of scores
        score.append(random_number_generator)

        # add 1 to iteration count at the end of loop
        iteration += 1

        # Test code to clear screen (provided by Gemini Pro)
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell = True)

        # ASCIIColor Table that refreshes for each round
        ASCIIColors.table(
            "[yellow]Roll #[/yellow]", "[yellow]Score[/yellow]",
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

    # create a final score variable that sums all values in the score list
    final_sum = sum(score)
    final_min = min(score)
    final_max = max(score)
    final_avg = sum(score) / len(score)

    # ASCIIColor Table for final score display
    ASCIIColors.table(
        "[green]Total rolls[/green]", "[green]Final Sum[/green]", "[green]Min[/green]", "[green]Max[/green]", "[green]Avg[/green]",
        rows=[
            [iteration, final_sum, final_min, final_max, final_avg],
        ],
        title=("[yellow]FINAL SCORES[/yellow]"),
        border_style="Yellow"
    )

    # Print final score (superceded by ASCIIColors table)
    #print(f"Final score : {final_score}")

    # Reset game query and
    reset_query = input("Do you want roll again? (y/n): ")
    if reset_query.lower() == "y":
        continue
    else:
        reset = False