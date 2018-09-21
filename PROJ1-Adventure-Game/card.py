from typing import List

import random


class Card:
    SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
    COLORS = ["red", "red", "black", "black"]
    VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    suit: int
    value: int

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return Card.VALUES[self.value] + " of " + Card.SUITS[self.suit]


class Deck:
    cards: List[Card] = []

    def __init__(self):
        for i in range(len(Card.SUITS)):
            for j in range(len(Card.VALUES)):
                self.cards.append(Card(i, j))

    def shuffle(self):
        new_cards: List[Card] = []
        chosen: List[int] = []

        for i in range(len(self.cards)):
            while True:
                i = random.randint(0, len(self.cards) - 1)

                if i in chosen:
                    break

                new_cards.append(self.cards[i])
                chosen.append(i)

        self.cards = new_cards

    def get_cards(self):
        return self.cards
