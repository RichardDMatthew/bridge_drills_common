import unittest

from framework.bid_machine import load_bid_table
from framework.bid_stack import BidStack, Positions
from cards.suit import Suits
from players.player import Player
from test_bids import open_1c, open_1d, open_1h, open_1s, respond_3h, respond_2d, respond_1nt, respond_2c, \
    respond_1h
from test_bids import respond_2s


class TestBook1Chapter5(unittest.TestCase):
    bid_table = load_bid_table('../bid_tables/acbl_series/')
    dealer = Positions.NORTH
    bids = BidStack(dealer)

    def test_example_1_page_135(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_2s()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3a'
        player.hand.suits[Suits.SPADE].cards = [14, 13, 10, 9, 8, 2]
        player.hand.suits[Suits.HEART].cards = [11, 10, 9]
        player.hand.suits[Suits.DIAMOND].cards = [5, 3]
        player.hand.suits[Suits.CLUB].cards = [13, 3]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_example_1_page_136(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_2s()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3a'
        player.hand.suits[Suits.SPADE].cards = [14, 12, 11, 7, 4, 2]
        player.hand.suits[Suits.HEART].cards = [14, 9]
        player.hand.suits[Suits.DIAMOND].cards = [7, 4, 2]
        player.hand.suits[Suits.CLUB].cards = [14, 6]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '3s')

    def test_example_2_page_136(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_2s()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3a'
        player.hand.suits[Suits.SPADE].cards = [13, 12, 10, 7, 6, 2]
        player.hand.suits[Suits.HEART].cards = [12, 4]
        player.hand.suits[Suits.DIAMOND].cards = [14, 13]
        player.hand.suits[Suits.CLUB].cards = [14, 11, 8]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 4)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '4s')

    def test_example_3_page_136(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1h()
        self.bids.push(bid)
        bid = respond_3h()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3c'
        player.hand.suits[Suits.SPADE].cards = [13, 9, 5]
        player.hand.suits[Suits.HEART].cards = [13, 11, 7, 5, 3]
        player.hand.suits[Suits.DIAMOND].cards = [14, 8, 2]
        player.hand.suits[Suits.CLUB].cards = [11, 7]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_example_1_page_137(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1h()
        self.bids.push(bid)
        bid = respond_3h()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3c'
        player.hand.suits[Suits.SPADE].cards = [10, 6]
        player.hand.suits[Suits.HEART].cards = [14, 12, 10, 6, 5, 3]
        player.hand.suits[Suits.DIAMOND].cards = [14, 12, 11, 8]
        player.hand.suits[Suits.CLUB].cards = [5]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 4)
        self.assertTrue(bid.strain == 'hearts')
        self.assertTrue(bid.bid == '4h')

    def test_example_2_page_137(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_2d()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3b'
        player.hand.suits[Suits.SPADE].cards = [12, 9, 7]
        player.hand.suits[Suits.HEART].cards = [11, 10]
        player.hand.suits[Suits.DIAMOND].cards = [14, 9, 8, 7, 6, 3]
        player.hand.suits[Suits.CLUB].cards = [13, 13]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_example_1_page_138(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_2d()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3b'
        player.hand.suits[Suits.SPADE].cards = [9, 8]
        player.hand.suits[Suits.HEART].cards = [9, 7]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 11, 6, 4, 2]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 12]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'diamonds')
        self.assertTrue(bid.bid == '3d')

    def test_example_2_page_138(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_2d()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3b'
        player.hand.suits[Suits.SPADE].cards = [14, 13, 7]
        player.hand.suits[Suits.HEART].cards = [13, 10, 4]
        player.hand.suits[Suits.DIAMOND].cards = [13, 11, 10, 7]
        player.hand.suits[Suits.CLUB].cards = [13, 12, 9]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '3nt')

    def test_example_1_page_139(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1h()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [13, 7, 3]
        player.hand.suits[Suits.HEART].cards = [14, 12, 10, 9, 5]
        player.hand.suits[Suits.DIAMOND].cards = [13, 10, 3]
        player.hand.suits[Suits.CLUB].cards = [8, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_example_2_page_139(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1h()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [12, 9, 8]
        player.hand.suits[Suits.HEART].cards = [13, 12, 6, 4, 3]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 8, 4]
        player.hand.suits[Suits.CLUB].cards = [3]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'diamonds')
        self.assertTrue(bid.bid == '2d')

    def test_example_3_page_139(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1h()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [9, 6, 2]
        player.hand.suits[Suits.HEART].cards = [14, 13, 10, 8, 6, 2]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 4]
        player.hand.suits[Suits.CLUB].cards = [6]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'hearts')
        self.assertTrue(bid.bid == '2h')

    def test_example_4_page_139(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1h()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [13, 10, 6, 4]
        player.hand.suits[Suits.HEART].cards = [14, 12, 11, 7, 6, 2]
        player.hand.suits[Suits.DIAMOND].cards = [12, 10]
        player.hand.suits[Suits.CLUB].cards = [5]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'hearts')
        self.assertTrue(bid.bid == '2h')

    def test_example_1_page_140(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [2]
        player.hand.suits[Suits.HEART].cards = [14, 8, 3]
        player.hand.suits[Suits.DIAMOND].cards = [14, 13, 11, 9, 7, 6]
        player.hand.suits[Suits.CLUB].cards = [14, 4, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'diamonds')
        self.assertTrue(bid.bid == '3d')

    def test_example_2_page_140(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [9]
        player.hand.suits[Suits.HEART].cards = [14, 13, 7, 2]
        player.hand.suits[Suits.DIAMOND].cards = [13, 11, 10, 8, 4]
        player.hand.suits[Suits.CLUB].cards = [14, 11, 5]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'hearts')
        self.assertTrue(bid.bid == '2h')

    def test_example_3_page_140(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [9]
        player.hand.suits[Suits.HEART].cards = [13, 11, 5]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 10, 6, 3]
        player.hand.suits[Suits.CLUB].cards = [14, 12, 11, 8]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'clubs')
        self.assertTrue(bid.bid == '2c')

    def test_example_1_page_141(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [14, 13, 11, 8, 7]
        player.hand.suits[Suits.HEART].cards = [10, 4, 2]
        player.hand.suits[Suits.DIAMOND].cards = [14, 12, 7]
        player.hand.suits[Suits.CLUB].cards = [14, 10]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '3nt')

    def test_example_2_page_141(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [13, 12, 11, 9, 7, 6, 3]
        player.hand.suits[Suits.HEART].cards = [5]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11]
        player.hand.suits[Suits.CLUB].cards = [14, 12, 11]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 4)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '4s')

    def test_example_3_page_141(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [14, 12, 10, 5, 3]
        player.hand.suits[Suits.HEART].cards = [9, 5]
        player.hand.suits[Suits.DIAMOND].cards = [14, 13, 11, 6]
        player.hand.suits[Suits.CLUB].cards = [14, 3]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'diamonds')
        self.assertTrue(bid.bid == '3d')

    def test_example_1_page_143(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_2s()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3a'
        player.hand.suits[Suits.SPADE].cards = [13, 11, 9, 8, 5, 4]
        player.hand.suits[Suits.HEART].cards = [14, 8, 6]
        player.hand.suits[Suits.DIAMOND].cards = [13, 9]
        player.hand.suits[Suits.CLUB].cards = [12, 4]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_example_2_page_143(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_2s()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3a'
        player.hand.suits[Suits.SPADE].cards = [14, 13, 11, 7, 5, 3]
        player.hand.suits[Suits.HEART].cards = [13, 12]
        player.hand.suits[Suits.DIAMOND].cards = [14, 12, 8]
        player.hand.suits[Suits.CLUB].cards = [5, 3]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 4)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '4s')

    def test_example_1_page_144(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1s()
        self.bids.push(bid)
        bid = respond_2s()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3a'
        player.hand.suits[Suits.SPADE].cards = [13, 12, 10, 9, 6, 2]
        player.hand.suits[Suits.HEART].cards = [5, 4]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 8]
        player.hand.suits[Suits.CLUB].cards = [14, 11]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '3s')

    def test_example_2_page_144(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1c()
        self.bids.push(bid)
        bid = respond_2c()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3b'
        player.hand.suits[Suits.SPADE].cards = [14, 12, 8, 5]
        player.hand.suits[Suits.HEART].cards = [13, 10, 6, 3]
        player.hand.suits[Suits.DIAMOND].cards = [11, 9]
        player.hand.suits[Suits.CLUB].cards = [12, 11, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_example_3_page_144(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1c()
        self.bids.push(bid)
        bid = respond_2c()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3b'
        player.hand.suits[Suits.SPADE].cards = [13, 3, 2]
        player.hand.suits[Suits.HEART].cards = [14, 7, 3]
        player.hand.suits[Suits.DIAMOND].cards = [3]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 11, 8, 6, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'clubs')
        self.assertTrue(bid.bid == '3c')

    def test_example_4_page_144(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1c()
        self.bids.push(bid)
        bid = respond_2c()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3b'
        player.hand.suits[Suits.SPADE].cards = [14, 11, 10]
        player.hand.suits[Suits.HEART].cards = [13, 11]
        player.hand.suits[Suits.DIAMOND].cards = [9, 7, 3]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 12, 11, 8]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '3nt')

    def test_example_5_page_144(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [9, 3]
        player.hand.suits[Suits.HEART].cards = [14]
        player.hand.suits[Suits.DIAMOND].cards = [14, 10, 8, 7, 3]
        player.hand.suits[Suits.CLUB].cards = [13, 12, 6, 4, 3]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'clubs')
        self.assertTrue(bid.bid == '2c')

    def test_example_6_page_144(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [14, 5]
        player.hand.suits[Suits.HEART].cards = [13, 11, 9]
        player.hand.suits[Suits.DIAMOND].cards = [14, 13, 7, 3, 2]
        player.hand.suits[Suits.CLUB].cards = [14, 5, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '3nt')

    def test_example_1_page_145(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [14, 12, 3]
        player.hand.suits[Suits.HEART].cards = [11, 8, 7]
        player.hand.suits[Suits.DIAMOND].cards = [14, 13, 12, 10, 6, 3]
        player.hand.suits[Suits.CLUB].cards = [6]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'diamonds')
        self.assertTrue(bid.bid == '3d')

    def test_example_2_page_145(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [12, 11, 10, 9]
        player.hand.suits[Suits.HEART].cards = [14, 3]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 9, 7, 6, 4]
        player.hand.suits[Suits.CLUB].cards = [5]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'diamonds')
        self.assertTrue(bid.bid == '2d')

    def test_example_3_page_145(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [14, 12]
        player.hand.suits[Suits.HEART].cards = [6, 2]
        player.hand.suits[Suits.DIAMOND].cards = [14, 12, 11, 8, 7]
        player.hand.suits[Suits.CLUB].cards = [13, 12, 11, 9]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'clubs')
        self.assertTrue(bid.bid == '3c')

    def test_example_4_page_145(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1nt()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3f'
        player.hand.suits[Suits.SPADE].cards = [13, 7]
        player.hand.suits[Suits.HEART].cards = [12, 11, 9, 2]
        player.hand.suits[Suits.DIAMOND].cards = [14, 8, 7, 4]
        player.hand.suits[Suits.CLUB].cards = [12, 11, 3]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_example_1_page_146(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1h()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3d'
        player.hand.suits[Suits.SPADE].cards = [14, 9, 3]
        player.hand.suits[Suits.HEART].cards = [13, 7, 6, 4]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 7, 3, 2]
        player.hand.suits[Suits.CLUB].cards = [9]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'hearts')
        self.assertTrue(bid.bid == '2h')

    def test_example_1_page_147(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1h()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3d'
        player.hand.suits[Suits.SPADE].cards = [12, 11, 9, 8]
        player.hand.suits[Suits.HEART].cards = [11, 8, 2]
        player.hand.suits[Suits.DIAMOND].cards = [14, 13, 11, 4]
        player.hand.suits[Suits.CLUB].cards = [12, 5]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 1)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '1s')

    def test_example_2_page_147(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1h()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3d'
        player.hand.suits[Suits.SPADE].cards = [13, 11, 10]
        player.hand.suits[Suits.HEART].cards = [11, 5]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 10, 9, 4]
        player.hand.suits[Suits.CLUB].cards = [14, 6, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 1)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '1nt')

    def test_example_3_page_147(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1d()
        self.bids.push(bid)
        bid = respond_1h()
        self.bids.push(bid)
        player = Player(Positions.NORTH)
        player.next_table = 'or3d'
        player.hand.suits[Suits.SPADE].cards = [14, 10, 8]
        player.hand.suits[Suits.HEART].cards = [5]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 10, 7, 3]
        player.hand.suits[Suits.CLUB].cards = [14, 11, 4, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'clubs')
        self.assertTrue(bid.bid == '2c')


if __name__ == '__main__':
    unittest.main()
    test_b1_c5 = TestBook1Chapter5()
