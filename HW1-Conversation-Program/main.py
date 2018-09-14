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
    colorResponses = ["Cool! That's mine too!", "Oh cool, mine's ", "I prefer "]
    colors = ["red", "green", "blue", "orange"]
    colorResponseNum = random.randint(0, len(colorResponses) - 1)
    colorIndex = random.randint(0, len(colors) - 1)
    while color.lower() == colors[colorIndex]:
        colorIndex = random.randint(0, len(colors)) 
    if colorResponseNum == 0: print(colorResponses[colorResponseNum])
    else: print(colorResponses[colorResponseNum] + colors[colorIndex] + ".")
    
    sports = ["soccer", "football", "baseball", "tennis", "hockey", "volleyball"]
    sportPlay = random.randint(0, len(sports))
    sportWatch = random.randint(0, len(sports))
    while sportPlay == sportWatch: sportWatch = random.randint(0, len(sports))
    favSport = ask("What's your favorite sport?")
    sports += favSport
    print("Cool, I play " + sports[sportPlay] + ", but I prefer to watch " + sports[sportWatch] + ".")
    
def ask(prompt):
    print(prompt)
    return input("> ")
    
main()