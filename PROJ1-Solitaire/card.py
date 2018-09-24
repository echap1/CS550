from typing import List
from termcolor import colored

import random


class Card:
    SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
    COLORS = ["red",   "red",      "black",  "black"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    suit: int
    value: int

    visible = True

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return Card.suitColored(Card.VALUES[self.value] + " of " + Card.SUITS[self.suit], self.suit)

    @staticmethod
    def suitColored(text: str, suit: int, attrs=["bold"]):
        if Card.COLORS[suit] == "black":
            return colored(text, attrs=attrs)

        return colored(text, Card.COLORS[suit], attrs=attrs)


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


class Location:
    pile_type: str
    pile_index: int
    pile_index2: int

    def __init__(self, pile_type, pile_index=0, pile_index2=-1):
        self.pile_type = pile_type
        self.pile_index = pile_index
        self.pile_index2 = pile_index2

    @staticmethod
    def is_location(loc_str):
        if loc_str == "":
            return False

        pile_type = loc_str[0]

        if not pile_type in "DHRF":
            return False

        if pile_type in "DHF":
            return True

        index_str = loc_str[2:]

        index_str = index_str.split(" ")

        if len(index_str) not in [1, 2]:
            return False

        try:
            [int(i) for i in index_str]

        except ValueError:
            return False

        return True

    @staticmethod
    def from_string(loc_str):
        pile_type = loc_str[0]

        if pile_type in "DH":
            return Location(pile_type)

        index_str = loc_str[2:]

        if index_str == "":
            pile_index = []

        else:
            pile_index = [int(i) for i in index_str.split(" ")] + [0]
            pile_index.pop()

        return Location(pile_type, *pile_index)
