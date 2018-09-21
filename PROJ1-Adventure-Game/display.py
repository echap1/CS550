from termcolor import colored

from card import *


class Display:

    @staticmethod
    def display_piles(piles: List[List[Card]]):
        pile_num = len(piles)
        max_str_len = len("10 of Diamonds")
        non_visible_str = colored("#" * max_str_len, "green")
        max_pile_len = max(*[len(i) for i in piles])

        line_str = ""

        for j in range(pile_num):
            card_str = "R" + str(j)
            card_str += " " * (max_str_len - len(card_str))

            line_str += colored(card_str, attrs=["bold", "underline"]) + " "

        print(line_str)

        for i in range(max_pile_len):
            line_str = ""

            for j in range(pile_num):
                if i >= len(piles[j]):
                    line_str += " " * max_str_len

                elif i != len(piles[j]) - 1:
                    line_str += non_visible_str

                else:
                    card_str = str(piles[j][i])
                    card_str += " " * (max_str_len - len(card_str))
                    card_color = Card.COLORS[piles[j][i].suit]
                    card_str = (colored(card_str, attrs=["bold"]) if card_color == "black" else
                                colored(card_str, card_color, attrs=["bold"]))

                    line_str += card_str

                line_str += " "

            print(line_str)