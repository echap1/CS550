"""
CS550 Project: Minesweeper
Due September 13, 2018

@author: Ethan Chapman
"""

import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

from libs.commandLine import CommandLine, Argument, VarInput, clear

from grid import Grid

c = CommandLine(__file__)
c.add_argument("WIDTH", Argument(int, lambda x: x > 0), "Width of the grid (1-26)")
c.add_argument("HEIGHT", Argument(int, lambda x: x > 0), "Height of the grid (1-26)")
c.add_argument("MINES", Argument(int, lambda x: x > 0), "Number of mines")

grid = Grid(*c.get_arg_values())

while True:
    print(grid)

    var_in = VarInput()

    x = var_in.input("Enter Position X: ", Argument(int, lambda x: 0 <= x < grid.w))
    y = var_in.input("Enter Position Y: ", Argument(int, lambda y: 0 <= y < grid.h))
    a = var_in.input("Enter Action (1: Check Square, 2: Toggle Flag)): ", Argument(int, lambda x: x in [1, 2]))

    clear()

    if a == 1:
        if grid.get_num(x, y) == -1:
            print("You Lose!")
            break

        if grid.get_visible(x, y):
            print("Square Visible!\n")

        grid.set_visible(x, y, True)

    if a == 2:
        grid.set_flagged(x, y, not(grid.get_flagged(x, y)))

    if grid.check_win():
        print("You Win!")
        break
