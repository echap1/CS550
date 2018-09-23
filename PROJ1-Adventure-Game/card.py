from typing import List
from termcolor import colored

import random


class Card:
    SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
    COLORS = ["red",   "red",      "black",  "black"]
    VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    suit: int
    value: int

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        if Card.COLORS[self.suit] == "black":
            return colored(Card.VALUES[self.value] + " of " + Card.SUITS[self.suit], attrs=["bold"])

        return colored(Card.VALUES[self.value] + " of " + Card.SUITS[self.suit], Card.COLORS[self.suit], attrs=["bold"])


class Deck:
    cards: List[Card] = []

    def __init__(self):
        for i in range(len(Card.SUITS)):
            for j in range(len(Card.VALUES)):
                self.cards.append(Card(i, j))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self):
        return self.cards
