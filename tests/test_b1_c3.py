import unittest

from bidding.bid_machine import load_bid_table
from bidding.bid_stack import BidStack, Positions
from cards.suit import Suits
from players.player import Player
from bidding.preload_bids import open_1nt


class TestBook1Chapter3(unittest.TestCase):
    bid_table = load_bid_table('../bidding/bid_tables/acbl_series/')
    dealer = Positions.NORTH
    bids = BidStack(dealer)

    def test_exercise_one_1(self):
        player = Player(Positions.NORTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [10, 8, 6, 5, 4, 2]
        player.hand.suits[Suits.HEART].cards = [11, 7, 5]
        player.hand.suits[Suits.DIAMOND].cards = [8]
        player.hand.suits[Suits.CLUB].cards = [11, 6, 2]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 2)
        self.assertTrue(player.hand.distribution_points == 2)
        self.assertTrue(player.hand.dist == 4)

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '2s')

    def test_exercise_one_2(self):
        player = Player(Positions.NORTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [11, 9, 2]
        player.hand.suits[Suits.HEART].cards = [14, 9, 6, 2]
        player.hand.suits[Suits.DIAMOND].cards = [11, 7, 6]
        player.hand.suits[Suits.CLUB].cards = [10, 9, 4]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 6)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 6)

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_exercise_one_3(self):
        player = Player(Positions.NORTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [12, 11]
        player.hand.suits[Suits.HEART].cards = [9, 8]
        player.hand.suits[Suits.DIAMOND].cards = [12, 9, 8]
        player.hand.suits[Suits.CLUB].cards = [10, 9, 7, 6, 3, 2]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 5)
        self.assertTrue(player.hand.distribution_points == 2)
        self.assertTrue(player.hand.dist == 7)

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 0)
        self.assertTrue(bid.strain == 'none')
        self.assertTrue(bid.bid == 'p')

    def test_exercise_two_1(self):
        player = Player(Positions.NORTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [12, 11,9, 7,6, 4]
        player.hand.suits[Suits.HEART].cards = [13, 8, 6]
        player.hand.suits[Suits.DIAMOND].cards = [13, 4, 3]
        player.hand.suits[Suits.CLUB].cards = [5]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 9)
        self.assertTrue(player.hand.distribution_points == 2)
        self.assertTrue(player.hand.dist == 11)

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 4)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '4s')

    def test_exercise_two_2(self):
        self.bids.reset(Positions.NORTH)
        player = Player(Positions.NORTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [14, 8, 2]
        player.hand.suits[Suits.HEART].cards = [14, 12, 9, 8, 3]
        player.hand.suits[Suits.DIAMOND].cards = [9, 4, 2]
        player.hand.suits[Suits.CLUB].cards = [10, 9]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 10)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 11)

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'hearts')
        self.assertTrue(bid.bid == '3h')

    def test_exercise_two_3(self):
        self.bids.reset(Positions.NORTH)
        player = Player(Positions.NORTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [12, 11]
        player.hand.suits[Suits.HEART].cards = [13, 12]
        player.hand.suits[Suits.DIAMOND].cards = [12, 9, 8]
        player.hand.suits[Suits.CLUB].cards = [11, 9, 7, 6, 3, 2]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 11)
        self.assertTrue(player.hand.distribution_points == 2)
        self.assertTrue(player.hand.dist == 13)

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '3nt')

    def test_exercise_seven_open(self):
        self.bids.reset(Positions.NORTH)
        player = Player(Positions.NORTH)
        player.next_table = 'or1'
        player.hand.suits[Suits.SPADE].cards = [13, 6, 5]
        player.hand.suits[Suits.HEART].cards = [14, 9, 7]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 11, 10]
        player.hand.suits[Suits.CLUB].cards = [14, 7, 5]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 1)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '1nt')

    def test_exercise_seven_response(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1nt()
        self.bids.push(bid)
        player = Player(Positions.SOUTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [14, 7, 3]
        player.hand.suits[Suits.HEART].cards = [13, 6, 2]
        player.hand.suits[Suits.DIAMOND].cards = [7, 5, 4, 2]
        player.hand.suits[Suits.CLUB].cards = [13, 6, 3]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 3)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '3nt')

    def test_exercise_eight_open(self):
        player = Player(Positions.NORTH)
        player.next_table = 'or1'
        player.hand.suits[Suits.SPADE].cards = [6, 5, 3]
        player.hand.suits[Suits.HEART].cards = [13, 12, 11]
        player.hand.suits[Suits.DIAMOND].cards = [13, 7, 5, 2]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 6]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 1)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '1nt')

    def test_exercise_eight_response(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1nt()
        self.bids.push(bid)
        player = Player(Positions.SOUTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [12, 11, 10, 9, 8, 7]
        player.hand.suits[Suits.HEART].cards = [8, 4, 2]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11]
        player.hand.suits[Suits.CLUB].cards = [5, 4]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 4)
        self.assertTrue(bid.strain == 'spades')
        self.assertTrue(bid.bid == '4s')

    def test_exercise_nine_open(self):
        self.bids.reset(Positions.NORTH)
        player = Player(Positions.NORTH)
        player.next_table = 'or1'
        player.hand.suits[Suits.SPADE].cards = [14, 13, 5, 3]
        player.hand.suits[Suits.HEART].cards = [14, 6, 4, 2]
        player.hand.suits[Suits.DIAMOND].cards = [12, 5]
        player.hand.suits[Suits.CLUB].cards = [13, 11, 6]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 1)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '1nt')

    def test_exercise_nine_response(self):
        self.bids.reset(Positions.NORTH)
        bid = open_1nt()
        self.bids.push(bid)
        player = Player(Positions.SOUTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [7, 6, 2]
        player.hand.suits[Suits.HEART].cards = [8, 7]
        player.hand.suits[Suits.DIAMOND].cards = [13, 11, 10, 6, 3]
        player.hand.suits[Suits.CLUB].cards = [14, 4, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '2nt')

    def test_exercise_ten_open(self):
        self.bids.reset(Positions.NORTH)
        player = Player(Positions.NORTH)
        player.next_table = 'or1'
        player.hand.suits[Suits.SPADE].cards = [14, 13, 5, 2]
        player.hand.suits[Suits.HEART].cards = [13, 12, 11]
        player.hand.suits[Suits.DIAMOND].cards = [8, 4]
        player.hand.suits[Suits.CLUB].cards = [14, 9, 3, 2]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 1)
        self.assertTrue(bid.strain == 'no trump')
        self.assertTrue(bid.bid == '1nt')

    def test_exercise_ten_response(self):
        self.bids.reset(Positions.NORTH)
        self.bids.reset(Positions.NORTH)
        bid = open_1nt()
        self.bids.push(bid)
        player = Player(Positions.SOUTH)
        player.next_table = 'or2d'
        player.hand.suits[Suits.SPADE].cards = [9, 6]
        player.hand.suits[Suits.HEART].cards = [6, 5, 4]
        player.hand.suits[Suits.DIAMOND].cards = [12, 11, 10, 9, 7, 6]
        player.hand.suits[Suits.CLUB].cards = [6, 4]

        player.hand.evaluate()

        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.level == 2)
        self.assertTrue(bid.strain == 'diamonds')
        self.assertTrue(bid.bid == '2d')


if __name__ == '__main__':
    unittest.main()
    test_b1_c3 = TestBook1Chapter3()
