from copy import deepcopy
import logging
import random

from cards.hand import Hand
from common import Suits, Positions

log = logging.getLogger('Bridge')


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:
    deal_count = 0

    def __init__(self):
        self.deck = [Card(value, suit) for value in range(2, 15) for suit in Suits]
        self.deal_deck = deepcopy(self.deck)  # used to deal out of

    def reset(self):
        del self.deal_deck
        self.deal_deck = deepcopy(self.deck)

    def shuffle(self):
        random.shuffle(self.deal_deck)

    def pop(self):
        return self.deal_deck.pop()

    def deal_to(self, players):
        self.deal_count += 1
        for card in range(0, 13):
            for player in players.players:
                card = self.deal_deck.pop()
                player.hand.add(card)

    def make_4_hands(self):
        hands = [Hand(Positions.NORTH, "none"), Hand(Positions.NORTH, "none"),
                 Hand(Positions.NORTH, "none"), Hand(Positions.NORTH, "none")]
        for card in range(0, 13):
            for hand in hands:
                card = self.deal_deck.pop()
                hand.add(card)
        return hands

    # todo: move all skill building code to separate area
    def deal_to_deal(self, deal):
        for card in range(0, 13):
            for hand in deal:
                card = self.deal_deck.pop()
                hand.add(card)

