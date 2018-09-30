"""
CS550 Homework: Number Game
Due September 14, 2018

@author: Ethan Chapman
"""

import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

from libs.varInput import VarInput


def invalid(value, params, valueError):
    if valueError:
        ask_for_n("No sir. Enter an integer: ")
    else:
        ask_for_n("No sir. That's not between 1 and 5. Try again: ")


varIn = VarInput(invalid)


def ask_for_n(message):
    varIn.input(message, int, lambda x: 1 <= x <= 5)


ask_for_n("Input a number between 1 and 5: ")
