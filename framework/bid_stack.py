import logging
from enum import IntEnum

log = logging.getLogger('Bridge')


class Positions(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class BidStack:
    def __init__(self, dealer):
        self.stack = []
        self.opened = False
        self.pass_counter = 0
        self.bidder = dealer
        self.golden_suit = [None, None, None, None]
        self.partners_suit = [None, None, None, None]
        self.last_bid_level = 0
        self.last_bid_strain = None
        self.dealer = dealer

    def reset(self, dealer):
        for _ in self.stack:
            del _
        self.stack = []
        self.opened = False
        self.pass_counter = 0
        self.dealer = dealer
        self.last_bid_level = 0
        self.last_bid_strain = None

    def push(self, bid):
        pass_out = False
        self.stack.append(bid)
        if bid.bid == 'p':
            self.pass_counter += 1
        else:
            self.opened = True
            self.pass_counter = 0
            self.last_bid_level = bid.level
            self.last_bid_strain = bid.strain

        if self.opened and self.pass_counter >= 4:
            pass_out = True
        elif self.pass_counter >= 3:
            pass_out = True

        return pass_out

    def get_partners_bids(self, position):
        partners_bids = []
        partner = get_partner(position)
        for bid in self.stack:
            if bid.bidder == partner:
                partners_bids.append(bid)
        return partners_bids

    def get_my_bids(self, my_position):
        my_bids = []
        for bid in self.stack:
            if bid.bidder == my_position:
                my_bids.append(bid)
        return my_bids

    def get_partners_strain(self, position):
        partners_bids = self.get_partners_bids(position)
        if len(partners_bids) > 0:
            partners_bid = partners_bids[len(partners_bids) - 1]
            partners_strain = partners_bid.strain
        else:
            partners_strain = 'none'
        return partners_strain

    def get_last_bid_value(self):
        strain_value = get_strain_value(self.last_bid_strain)
        last_bid_value = (int(self.last_bid_level) * 10) + strain_value
        return last_bid_value


class Bid:
    def __init__(self, bidder, table_id, bid, level, strain, next_table, description, reference, comments=None):
        self.bidder = bidder
        self.table_id = table_id
        self.bid = bid
        self.level = level
        self.strain = strain
        self.next_table = next_table
        self.description = description
        self.reference = reference
        self.comments = comments


conventions = {'none': True,
               'stayman': False,
               'jacoby': False,
               'blackwood': False,
               'gerber': False,
               'preempt': True}


def print_bid(bid):
    print('--------------------------------------------------------------')
    print('bidder:', bid.bidder, 'table:', bid.table_id, 'bid:', bid.bid)
    print('description:', bid.description)
    print('reference:', bid.reference)
    print('comments:', bid.comments)
    print('--------------------------------------------------------------')


def get_right_opponent(player):
    if player == Positions.NORTH:
        return Positions.WEST
    elif player == Positions.EAST:
        return Positions.NORTH
    elif player == Positions.SOUTH:
        return Positions.EAST
    else:
        return Positions.SOUTH


def get_partner(player):
    if player == Positions.NORTH:
        return Positions.SOUTH
    elif player == Positions.EAST:
        return Positions.WEST
    elif player == Positions.SOUTH:
        return Positions.NORTH
    else:
        return Positions.EAST


def get_strain_value(strain):
    if strain == 'none':
        strain_value = 0
    elif strain == 'clubs':
        strain_value = 1
    elif strain == 'diamonds':
        strain_value = 2
    elif strain == 'hearts':
        strain_value = 3
    elif strain == 'spades':
        strain_value = 4
    else:    # strain == 'no trump':
        strain_value = 5
    return strain_value


def get_candidate_bid_value(level, strain):
    strain_value = get_strain_value(strain)
    candidate_bid_value = (level * 10) + strain_value
    return candidate_bid_value

