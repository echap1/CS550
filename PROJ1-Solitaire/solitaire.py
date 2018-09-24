"""
CS550 Project: Solitaire
Due September 24, 2018

@author: Ethan Chapman

Dependencies:
    termcolor - package for changing the console colors
    pyparsing - parsing colored strings
"""

from display import Display
from game import Game

game = Game()

while sum([len(i) for i in game.piles]) > 0:
    Display.clear()
    Display.display(game)
    game.do_turn()

print("You Win!")