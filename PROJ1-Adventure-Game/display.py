from card import *
from pyparsing import *


class Display:

    @staticmethod
    def display(deck: List[Card], hand: List[Card], piles: List[List[Card]]):
        Display.display_hand(deck, hand)
        print()
        Display.display_piles(piles)

    @staticmethod
    def display_hand(deck: List[Card], hand: List[Card]):
        max_str_len = len("10 of Diamonds")
        non_visible_str = colored("#" * max_str_len, "green")

        print(colored(Display.__to_length("(D)eck", max_str_len), attrs=["bold", "underline"]) + " " +
              colored(Display.__to_length("(H)and", max_str_len), attrs=["bold", "underline"]))

        deck_str: List[str] = []

        i = len(deck)

        while i != 0:
            if i - max_str_len >= 0:
                deck_str += ["#" * max_str_len]
                i -= max_str_len

            else:
                deck_str += [Display.__to_length("#" * i, max_str_len)]
                i = 0

        deck_str = [colored(i, "green") for i in deck_str]

        hand_str: List[str] = []

        for i in range(len(hand)):
            if i == len(hand) - 1:
                hand_str += [colored(str(hand[i]), attrs=["underline"])]

            else:
                hand_str += [str(hand[i])]

        max_lines = max(len(deck_str), len(hand_str))

        for i in range(max_lines):
            line_str = ""

            if len(deck_str) > i:
                line_str += deck_str[i]

            else:
                line_str += Display.__to_length("", max_str_len)

            line_str += " "

            if len(hand_str) > i:
                line_str += hand_str[i]

            print(line_str)

    @staticmethod
    def display_piles(piles: List[List[Card]]):
        pile_num = len(piles)
        max_str_len = len("10 of Diamonds")
        non_visible_str = colored("#" * max_str_len, "green")
        max_pile_len = max(*[len(i) for i in piles])

        line_str = ""

        for j in range(pile_num):
            card_str = Display.__to_length("R" + str(j), max_str_len)

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
                    card_str = Display.__to_length(str(piles[j][i]), max_str_len)

                    line_str += card_str

                line_str += " "

            print(line_str)

    @staticmethod
    def __to_length(s: str, n: int):
        ESC = LiteraESC = Literal('\x1b')
        integer = Word(nums)
        escapeSeq = Combine(ESC + '[' + Optional(delimitedList(integer, ';')) +
                            oneOf(list(alphas)))

        nonAnsiString = lambda s: Suppress(escapeSeq).transformString(s)('\x1b')
        integer = Word(nums)
        escapeSeq = Combine(ESC + '[' + Optional(delimitedList(integer, ';')) +
                            oneOf(list(alphas)))

        nonAnsiString = lambda s: Suppress(escapeSeq).transformString(s)

        s_len = len(nonAnsiString(s))

        return s + " " * (n - s_len)