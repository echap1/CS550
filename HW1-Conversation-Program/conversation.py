"""
CS550 Homework: Conversation Program
Due September 10, 2018

@author: Ethan Chapman

Sources:

"""

import random


def main():
    name = ask("Hi, what's your name?")
    print("Nice to meet you, " + name + ".")

    color = ask("What's your favorite color?")
    color_responses = ["Cool! That's mine too!", "Oh cool, mine's ", "I prefer "]
    colors = ["red", "green", "blue", "orange"]
    color_response_num = random.randint(0, len(color_responses) - 1)
    color_index = random.randint(0, len(colors) - 1)
    while color.lower() == colors[color_index]:
        color_index = random.randint(0, len(colors))
    if color_response_num == 0:
        print(color_responses[color_response_num])
    else:
        print(color_responses[color_response_num] + colors[color_index] + ".")

    sports = ["soccer", "football", "baseball", "tennis", "hockey", "volleyball"]
    sport_play = random.randint(0, len(sports))
    sport_watch = random.randint(0, len(sports))

    while sport_play == sport_watch:
        sport_watch = random.randint(0, len(sports))

    fav_sport = ask("What's your favorite sport?")
    sports += fav_sport
    print("Cool, I play " + sports[sport_play] + ", but I prefer to watch " + sports[sport_watch] + ".")


def ask(prompt):
    print(prompt)
    return input("> ")


main()
