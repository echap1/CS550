import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

from typing import List
from termcolor import colored

from libs.commandLine import VarInput, Argument

from card import Card, Deck, Location


class Game:
    PILES = 7

    varInput: VarInput

    deck: List[Card]
    hand: List[Card]
    piles: List[List[Card]]
    finished: List[int]

    inputStrings = {"D": "(D)eck",
                    "H": "(H)and",
                    "R": "(R (0-" + str(PILES) + ") (Pile Position))",
                    "F": "(F)inished"}

    def __init__(self):
        deck = Deck()

        deck.shuffle()

        deck = deck.get_cards()

        piles: List[List[Card]] = []

        for i in range(Game.PILES):
            piles.append([])
            pile_len = i + 1

            for j in range(pile_len):
                card = deck.pop()

                if not j == pile_len - 1:
                    card.visible = False

                piles[i].append(card)

        hand: List[Card] = []

        self.varInput = VarInput()

        self.deck = deck
        self.hand = hand
        self.piles = piles
        self.finished = [0] * len(Card.SUITS)

    def do_turn(self):
        in_loc = self.input_location("DHR")

        if in_loc.pile_type == "R":
            to_loc = self.input_location("RF")

            if to_loc.pile_type == "R":
                self.move_pile_pile(in_loc, to_loc)
                return

            if to_loc.pile_type == "F":
                self.move_pile_finished(in_loc)
                return

        if in_loc.pile_type == "H":
            to_loc = self.input_location("RF")

            if to_loc.pile_type == "R":
                self.move_hand_pile(to_loc)
                return

            if to_loc.pile_type == "F":
                self.move_hand_finished()
                return

        if in_loc.pile_type == "D":
            if len(self.deck) == 0:
                self.deck = self.hand[::-1]

                self.hand = []

            self.hand += [self.deck.pop()]

            print("Success!")

    def move_pile_pile(self, loc1: Location, loc2: Location):
        if len(self.piles[loc1.pile_index]) == 0:
            print("Invalid Move!")
            return

        num1 = loc1.pile_index
        num2 = loc2.pile_index
        index1 = loc1.pile_index2

        if num1 == num2:
            return

        if not all([i.visible for i in self.piles[num1][index1:]]):
            print("Invalid Move!")

            return

        pile1 = self.piles[num1][index1:]
        self.piles[num1] = self.piles[num1][:index1]

        card1 = pile1[0]

        if len(self.piles[num2]) != 0:
            card2 = self.piles[num2][-1]

            if (Card.COLORS[card1.suit] != Card.COLORS[card2.suit] and
                    card1.value + 1 == card2.value):
                self.piles[num2] += pile1

                if len(self.piles[num1]) > 0:
                    self.piles[num1][-1].visible = True

                print("Success!")

            else:
                print("Invalid Move!")

                self.piles[num1] += pile1

        else:
            if card1.value == len(Card.VALUES) - 1:
                self.piles[num2] += pile1

                if len(self.piles[num1]) > 0:
                    self.piles[num1][-1].visible = True

                print("Success!")

            else:
                print("Invalid Move!")

                self.piles[num1] += pile1

    def move_hand_pile(self, pile_loc):
        if len(self.hand) == 0:
            print("Invalid Move!")
            return

        pile_num = pile_loc.pile_index

        if len(self.piles[pile_num]) == 0:
            if self.hand[-1].value == len(Card.VALUES) - 1:
                card = self.hand.pop()
                card.visible = True

                self.piles[pile_num] += [card]

                print("Success")

            else:
                print("Invalid Move!")

        else:
            card1 = self.hand.pop()
            card2 = self.piles[pile_num].pop()

            if (Card.COLORS[card1.suit] != Card.COLORS[card2.suit] and
                    card1.value + 1 == card2.value):
                self.piles[pile_num] += [card2, card1]

                print("Success!")

            else:
                print("Invalid Move!")

                self.hand += [card1]
                self.piles[pile_num] += [card2]

    def move_pile_finished(self, pile_loc):
        if len(self.piles[pile_loc.pile_index]) == 0:
            print("Invalid Move!")
            return

        finished_card = self.piles[pile_loc.pile_index].pop()

        if self.finished[finished_card.suit] == finished_card.value:
            self.finished[finished_card.suit] += 1

            print("Success!")

            if len(self.piles[pile_loc.pile_index]) != 0:
                self.piles[pile_loc.pile_index][-1].visible = True

        else:
            self.piles[pile_loc.pile_index] += [finished_card]

            print("Invalid Move!")

    def move_hand_finished(self):
        if len(self.hand) == 0:
            print("Invalid Move!")
            return

        finished_card = self.hand.pop()

        if self.finished[finished_card.suit] == finished_card.value:
            self.finished[finished_card.suit] += 1

            print("Success!")

        else:
            self.hand += [finished_card]

            print("Invalid Move!")

    def input_location(self, places, message=None):
        if message is None:
            message = colored("Input (" + ", ".join([self.inputStrings[s] for s in places]) + "): ", "blue", attrs=["bold"])

        while True:
            loc = Location.from_string(self.varInput.input(message, Argument(str, Location.is_location)))

            if loc.pile_type in places:
                break

        return loc
