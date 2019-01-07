"""
CS550 Homework: Monty Hall Simulation
Due January 9, 2019

@author: Ethan Chapman

Thoughts:
    You have a 1/3 chance of picking the right door on the first try and a 2/3 chance that it is in another door.
    When the host shows you a penny in one of the remaining doors, there is still a 1/3 chance that you picked the
    right door on the first try, so there must be a 2/3 chance that it is in the other door.

Thoughts After Running:
    This is what I expected.
"""

import random

trials = 1000

def no_switch():
    successes = 0

    for _ in range(trials):  # 1000 iterations
        door_chosen = 1  # Making this random won't affect results
        prize_door = random.randint(1, 3)  # Choose random door for results

        if door_chosen == prize_door:  # If you chose the prize door, you won't switch out of it and you will win
            successes += 1

    return successes / trials


def switch():
    successes = 0

    for _ in range(trials):  # 1000 iterations
        door_chosen = 1  # Making this random won't affect results
        prize_door = random.randint(1, 3)  # Choose random door for results

        # If you didn't choose the prize door, the host will reveal the other door, and you will switch to the prize
        if door_chosen != prize_door:
            successes += 1

    return successes / trials

print(f"No Switch: {round(no_switch() * 1000) / 10}%")
print(f"Switch: {round(switch() * 1000) / 10}%")
