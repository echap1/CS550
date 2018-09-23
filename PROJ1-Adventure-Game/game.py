from typing import List

from card import Card, Deck


def setup():
    deck = Deck()

    deck.shuffle()

    unplacedCards = deck.get_cards()

    piles: List[List[Card]] = []
    pileNum = 7

    for i in range(pileNum):
        piles.append([])
        pileLen = i + 1

        for j in range(pileLen):
            piles[i].append(unplacedCards.pop())

    hand: List[Card] = []

    return [unplacedCards, hand, piles]