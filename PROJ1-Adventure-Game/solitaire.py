import sys
sys.path.append("..")

from display import Display

import game

[deck, hand, piles] = game.setup()

Display.display(deck, hand, piles)
