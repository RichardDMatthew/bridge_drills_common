import logging
from enum import IntEnum

log = logging.getLogger('Bridge')

face_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Suits(IntEnum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class Strains(IntEnum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3
    NO_TRUMP = 4


class Strains(IntEnum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3
    NO_TRUMP = 4


def strain_to_symbol(strain):
    if strain == Strains.CLUBS:
        return 'C'
    elif strain == Strains.DIAMONDS:
        return 'D'
    elif strain == Strains.HEARTS:
        return 'H'
    elif strain == Strains.SPADES:
        return 'S'
    else:
        return 'NT'


def suit_to_strain(suit):
    if suit == Suits.CLUB:
        return Strains.CLUBS
    elif suit == Suits.DIAMOND:
        return Strains.DIAMONDS
    elif suit == Suits.HEART:
        return Strains.HEARTS
    elif suit == Suits.SPADE:
        return Strains.SPADES
    else:  # isn't in Suit class so assuming in Strain class so just return it
        return suit


def strain_to_suit(strain):
    if strain == Strains.CLUBS:
        return Suits.CLUB
    elif strain == Strains.DIAMONDS:
        return Suits.DIAMOND
    elif strain == Strains.HEARTS:
        return Strains.HEARTS
    elif strain == Strains.SPADES:
        return Suits.SPADE
    else:
        return None


def is_major(suit):
    if suit == Strains.NO_TRUMP or suit == Strains.CLUBS or suit == Strains.DIAMONDS:
        return False
    elif suit == Suits.CLUB or suit == Suits.DIAMOND:
        return False
    else:
        return True


def get_suit_name(suit):
    if suit == Suits.SPADE:
        return 'Spades'
    elif suit == Suits.HEART:
        return 'Hearts'
    elif suit == Suits.DIAMOND:
        return 'Diamonds'
    elif suit == Suits.CLUB:
        return 'Clubs'


def get_highest_suit(suit_1, suit_2):
    if suit_1.suit > suit_2.suit:
        return suit_1
    else:
        return suit_2


class Suit:
    def __init__(self, suit):
        self.is_major = False
        self.suit = suit
        if self.suit == Suits.HEART or self.suit == Suits.SPADE:
            self.is_major = True
        self.cards = []
        self.high_card_points = 0
        self.distribution_points = 0
        self.short_suit_points = 0
        self.total_points = 0
        self.length = 0
        self.stopper = False

        # honors
        self.honors = 0
        self.protected_honors = 0
        self.high_honors = 0

    def reset(self):
        while self.cards:
            dump = self.cards.pop()
            del dump
        self.clear()
        self.is_major = False
        if self.suit == Suits.HEART or self.suit == Suits.SPADE:
            self.is_major = True

    def clear(self):
        self.high_card_points = 0
        self.distribution_points = 0
        self.short_suit_points = 0
        self.total_points = 0
        self.length = 0
        self.stopper = False

        # honors
        self.honors = 0
        self.high_honors = 0
        self.protected_honors = 0

    def count_high_card_points(self):
        self.high_card_points = 0
        # if not Config.adjust_HC_pnts_for_short_suits:
        for value in self.cards:
            if value > 10:
                self.high_card_points += value - 10

        # # this gets a little complex because high card points are affected by suit length
        # if len(self.cards) >= 3:  # can use A K Q J
        #     for value in self.cards:
        #         if value >= 11:
        #             print(value)
        #             self.high_card_points += value - 10
        #
        # elif len(self.cards) == 2:
        #     for value in self.cards:
        #         if value >= 13:
        #             print(value)
        #             self.high_card_points += value - 10
        #         elif value == 4 and self.high_card_points == 4:
        #             self.high_card_points += 2
        #         elif value == 3 and self.high_card_points == 3:
        #             self.high_card_points += 1
        #
        # elif len(self.cards) == 1:
        #     if 14 in self.cards:
        #         self.high_card_points += 4
        #     elif 13 in self.cards:
        #         self.high_card_points += 2
        #     elif 12 in self.cards:
        #         self.high_card_points += 1

    def count_distribution_points(self):
        self.distribution_points = 0
        if len(self.cards) > 4:
            self.distribution_points = len(self.cards) - 4

    def count_short_suit_points(self):
        self.short_suit_points = 0
        if len(self.cards) < 4:
            self.short_suit_points = 3 - len(self.cards)

    def add(self, value):
        self.cards.append(value)

    def sort(self):
        self.cards.sort(reverse=True)

    def list(self):
        suit_output = get_suit_name(self.suit)
        for value in self.cards:
            suit_output += ' ' + face_value[value]

        return suit_output

    def get_bid_table_name(self):
        if self.suit == Suits.SPADE:
            return "spades"
        elif self.suit == Suits.HEART:
            return "hearts"
        elif self.suit == Suits.DIAMOND:
            return "diamonds"
        else:
            return "clubs"

    def has_stopper(self):
        for value in self.cards:
            if value == 14:  # Ace
                return True
            elif value == 13 and self.length > 1:  # King and one backer
                return True
            elif value == 12 and self.length > 2:  # Queen and 2 backers
                return True
            elif value == 11 and self.length > 3:  # Jack and 3 backers
                return True
        return False

    def count_honors(self):
        protected_honors = 0
        for value in self.cards:
            if value > 9:
                self.honors += 1
            if value >= 12:
                self.high_honors += 1
            if value == 14:  # Ace
                protected_honors += 1
            elif value == 13 and self.length > 1:  # King and one backer
                protected_honors += 1
            elif value == 12 and self.length > 2:  # Queen and 2 backers
                protected_honors += 1
            elif value == 11 and self.length > 3:  # Jack and 3 backers
                protected_honors += 1
        self.protected_honors = protected_honors

    def evaluate(self):
        self.clear()
        self.cards.sort(reverse=True)
        self.count_high_card_points()
        self.count_distribution_points()
        self.count_short_suit_points()
        self.length = len(self.cards)
        self.stopper = self.has_stopper()
        self.count_honors()


def get_other_maj_or_min(suit):
    if suit == Suits.SPADE:
        return Suits.HEART
    elif suit == Suits.HEART:
        return Suits.SPADE
    elif suit == Suits.DIAMOND:
        return Suits.CLUB
    elif suit == Suits.CLUB:
        return Suits.DIAMOND


def get_suit_value(suit_name):
    if suit_name == 'spades':
        return Suits.SPADE
    elif suit_name == "hearts":
        return Suits.HEART
    elif suit_name == 'diamonds':
        return Suits.DIAMOND
    elif suit_name == 'clubs':
        return Suits.CLUB

