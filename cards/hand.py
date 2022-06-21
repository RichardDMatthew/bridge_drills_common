import logging
from copy import deepcopy

from framework.bid_stack import Positions
from cards.suit import Suit, Suits
# from player import get_partner

log = logging.getLogger('Bridge')


def build_hand(spades, hearts, diamonds, clubs):
    test_hand = Hand(Positions.NORTH)
    from cards.suit import Suit
    test_hand.suits[Suits.SPADE] = Suit(Suits.SPADE)
    test_hand.suits[Suits.SPADE].cards = spades
    test_hand.suits[Suits.HEART] = Suit(Suits.HEART)
    test_hand.suits[Suits.HEART].cards = hearts
    test_hand.suits[Suits.DIAMOND] = Suit(Suits.DIAMOND)
    test_hand.suits[Suits.DIAMOND].cards = diamonds
    test_hand.suits[Suits.CLUB] = Suit(Suits.CLUB)
    test_hand.suits[Suits.CLUB].cards = clubs
    test_hand.evaluate()
    return test_hand


def make_suits_by_length(list_of_suits):
    # We start from 1 since the first element is trivially sorted
    # bubble sort
    # todo: try quick sort, timsort or merge sort
    # todo: look for a sort that can sort a list of classes by one of the classes attributes
    for current_position, current_suit in enumerate(list_of_suits):

        while current_position > 0 and list_of_suits[current_position - 1].length < current_suit.length:
            list_of_suits[current_position] = list_of_suits[current_position - 1]
            current_position = current_position - 1

        list_of_suits[current_position] = current_suit
    return list_of_suits

    # for index in range(len(list_of_suits)):  # 0 - 3
    #     current_suit = list_of_suits[index]
    #     current_position = index
    #
    #     while current_position > 0 and list_of_suits[current_position - 1].length < current_suit.length:
    #         list_of_suits[current_position] = list_of_suits[current_position - 1]
    #         current_position = current_position - 1
    #
    #     list_of_suits[current_position] = current_suit
    # return list_of_suits


def get_highest_longest_major(hand):
    if hand.suits[Suits.SPADE].length >= hand.suits[Suits.HEART].length:  # returns the highest ranking equal suit
        return hand.suits[Suits.SPADE]
    else:
        return hand.suits[Suits.HEART]


def get_lowest_longest_major(hand):
    if hand.suits[Suits.HEART].length >= hand.suits[Suits.SPADE].length:  # returns the highest ranking equal suit
        return hand.suits[Suits.HEART]
    else:
        return hand.suits[Suits.SPADE]


def get_shortest_major(hand):
    if hand.suits[Suits.SPADE].length < hand.suits[Suits.HEART].length:
        return hand.suits[Suits.SPADE]
    else:
        return hand.suits[Suits.HEART]


class Hand:
    def __init__(self, position, convention):
        self.position = position
        self.convention = convention
        self.suits = [Suit(name) for name in Suits]
        self.high_card_points = 0
        self.distribution_points = 0
        self.short_suit_points = 0
        self.dummy_points = 0   # high card points plus
        self.adjustment_points = 0
        self.balanced = False
        self.five_card_major = False
        self.four_card_minor = False
        self.worthless_doubleton = False
        self.stoppers = []
        self.suits_by_length = []
        self.open = None
        self.active_bidder = False
        # new vars for bid table
        self.dist = 0
        self.shape = ''
        self.stopped_suits = 0
        self.hcp = 0
        self.previous_bids = ['none']

    def reset(self):
        for suit in self.suits:
            suit.reset()
        self.clear()

    def clear(self):
        self.high_card_points = 0
        self.distribution_points = 0
        self.short_suit_points = 0
        self.dummy_points = 0
        self.balanced = False
        self.five_card_major = False
        self.four_card_minor = False
        self.worthless_doubleton = False
        while self.stoppers:
            dump = self.stoppers.pop()
            del dump
        while self.suits_by_length:
            dump = self.suits_by_length.pop()
            del dump
        self.open = None
        self.active_bidder = False
        # new vars for bid table
        self.dist = 0
        self.shape = ''
        self.stopped_suits = 0
        self.hcp = 0

    def add(self, card):
        self.suits[card.suit].add(card.value)

    def check_for_shape(self):  # walks through suits to check for signatures of a balanced hand
        # there are 'balanced' and 'skewed' hands
        # a 'balanced' hand can also be 'flat'
        # a 'skewed' hand can also be 'two suited'
        # balanced is no voids or singletons and only on doubleton
        # a flat balanced hand is 4, 3, 3, 3
        # a skewed hand has a void, a singleton or two doubletons
        # a two suited skewed hand does not have 2 - 4 card suits, those are three suited
        self.shape = 'skew'
        numb_doubles: int = 0
        for suit in self.suits:
            if suit.length < 2:  # a balanced had has no voids or singles
                return
            if suit.length == 2:  # a balanced hand has no more than one double
                numb_doubles += 1
                if numb_doubles > 1:
                    return
        self.shape = 'bal'
        self.balanced = True
        return

    def evaluate(self):
        self.clear()
        for suit in self.suits:
            suit.evaluate()
            self.high_card_points += suit.high_card_points
            self.distribution_points += suit.distribution_points
            self.short_suit_points += suit.short_suit_points

            if suit.is_major and suit.length > 4:
                self.five_card_major = True
            if not suit.is_major and suit.length > 3:
                self.four_card_minor = True
            if suit.stopper:
                self.stoppers.append(suit.suit)
                self.stopped_suits += 1
            if suit.length <= 2 and suit.high_card_points == 0:
                self.worthless_doubleton = True

        suits_by_length = deepcopy(self.suits)
        self.suits_by_length = make_suits_by_length(suits_by_length)
        self.check_for_shape()
        self.hcp = self.high_card_points
        self.dist = self.high_card_points + self.distribution_points
        # todo: include -1 for no aces, -1 for no biddable suit, unsupported honors -1

    def adjust_evaluation(self, bid):
        # adjust for honors, in RHO's suit +1, in LHO's suit -1, in partner's suit +1v
        pass

    def get_next_best_suit(self, suit):
        index = 0
        while self.suits_by_length[index].suit != suit.suit:
            tmp = self.suits_by_length[index].suit
            index += 1
        # if the end of the list has been reached index is at null suit return that, otherwise next one in line
        tmp = self.suits_by_length[index].suit
        if index == 3:
            return self.suits_by_length[index]
        else:
            return self.suits_by_length[index + 1]

    def sort(self):
        for suit in self.suits:
            suit.sort()

    def set_dummy_points(self, bid_suit):
        self.dummy_points = 0
        b_suit = ''
        # todo: clean this up
        if bid_suit == "clubs":
            b_suit = Suits.CLUB
        elif bid_suit == "diamonds":
            b_suit = Suits.DIAMOND
        elif bid_suit == "hearts":
            b_suit = Suits.HEART
        elif bid_suit == "spades":
            b_suit = Suits.SPADE

        for suit in self.suits:
            if suit.suit == b_suit:
                continue    # don't count dummy points for bid.strain
            else:
                if suit.length == 0:
                    self.dummy_points += 5
                elif suit.length == 1:
                    self.dummy_points += 3
                elif suit.length == 2:
                    self.dummy_points += 1
                else:
                    continue
        self.dummy_points += self.high_card_points

    def stoppers_in_other_suits(self, bid_suit):
        stopper_count = 0
        for suit in self.suits:
            if suit.suit == bid_suit:
                continue
            if suit.stopper:
                stopper_count += 1
        return stopper_count

    def print(self):
        for suit in reversed(Suits):
            print(self.suits[suit].list())

    def print_description(self):
        print('hcp', self.high_card_points, 'dist', self.distribution_points, 'adj', self.adjustment_points)
        print('shape', self.shape)

    def is_partner_of(self, player):
        if self.position == Positions.NORTH and player == Positions.SOUTH:
            return True
        elif self.position == Positions.EAST and player == Positions.WEST:
            return True
        elif self.position == Positions.SOUTH and player == Positions.NORTH:
            return True
        elif self.position == Positions.WEST and player == Positions.EAST:
            return True
        else:
            return False

    def my_partner(self):
        if self.position == Positions.NORTH:
            return Positions.SOUTH
        elif self.position == Positions.EAST:
            return Positions.WEST
        elif self.position == Positions.SOUTH:
            return Positions.NORTH
        else:
            return Positions.EAST


