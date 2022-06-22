# players have hands
import logging

from bidding.bid_machine import bid_machine
from bidding.bid_stack import Positions
from cards.hand import Hand

log = logging.getLogger('Bridge')


# todo: later on set this up as a configurable option
def set_convention(pair):
    if pair == 'ns':
        return {'none': True, 'stayman': False, 'jacoby': False, 'blackwood': False, 'gerber': False,
                'preempt': True}
    else:
        return {'none': True, 'stayman': False, 'jacoby': False, 'blackwood': False, 'gerber': False,
                'preempt': True}


class Player:
    def __init__(self, position):
        self.next_table = 'or1'     # all next bid bid_tables are opener until one actually does
        self.position = position
        self.convention = None
        self.hand = Hand(self.position, self.convention)
        if position == Positions.NORTH or Positions.SOUTH:
            self.convention = set_convention('ns')
            self.hand.convention = self.convention
        else:
            self.convention = set_convention('ew')
            self.hand.convention = self.convention

    def reset(self):
        self.hand.reset()

    def organize_hand(self):
        #   This function has no test case because of it's simplicity, hand.sort and hand.evaluate are tested elsewhere
        self.hand.sort()
        self.hand.evaluate()

    def do_bid(self, bids, bid_table):
        bid_df = bid_table[bid_table["table id"] == self.next_table]
        bid = bid_machine(self.hand, bids, bid_df)
        return bid

    def do_play(self):
        pass
