import unittest

from bidding.bid_machine import load_bid_table
from bidding.bid_stack import BidStack, Positions
from cards.hand import Hand
from cards.suit import Suits
from players.player import Player


class TestBook1Chapter2(unittest.TestCase):
    bid_table = load_bid_table('../bidding/bid_tables/acbl_series/')
    dealer = Positions.NORTH
    bids = BidStack(dealer)

    def test_exercise_one_1(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [10, 9, 8, 6, 5, 3]
        hand.suits[Suits.HEART].cards = [14, 13, 12]
        hand.suits[Suits.DIAMOND].cards = [9, 8]
        hand.suits[Suits.CLUB].cards = [12, 11]

        hand.evaluate()
        self.assertTrue(hand.hcp == 12)
        self.assertTrue(hand.distribution_points == 2)
        self.assertTrue(hand.dist == 14)

    def test_exercise_one_2(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [14, 12, 11]
        hand.suits[Suits.HEART].cards = [9, 6, 4, 3, 2]
        hand.suits[Suits.DIAMOND].cards = [11, 9, 4, 3]
        hand.suits[Suits.CLUB].cards = [9]

        hand.evaluate()
        self.assertTrue(hand.hcp == 8)
        self.assertTrue(hand.distribution_points == 1)
        self.assertTrue(hand.dist == 9)

    def test_exercise_one_3(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [8, 6, 3]
        hand.suits[Suits.HEART].cards = [14, 12, 11, 9]
        hand.suits[Suits.DIAMOND].cards = [13, 9, 8]
        hand.suits[Suits.CLUB].cards = [14, 13, 12]

        hand.evaluate()
        self.assertTrue(hand.hcp == 19)
        self.assertTrue(hand.distribution_points == 0)
        self.assertTrue(hand.dist == 19)

    def test_exercise_two_1(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [13, 11, 7, 3]
        hand.suits[Suits.HEART].cards = [14, 9, 5]
        hand.suits[Suits.DIAMOND].cards = [12, 11, 6]
        hand.suits[Suits.CLUB].cards = [14, 11, 10]

        hand.evaluate()
        self.assertTrue(hand.balanced)

    def test_exercise_two_2(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [11, 7]
        hand.suits[Suits.HEART].cards = [13, 9, 7, 4]
        hand.suits[Suits.DIAMOND].cards = [13, 12, 10, 5]
        hand.suits[Suits.CLUB].cards = [14, 11, 8]

        hand.evaluate()
        self.assertTrue(hand.balanced)

    def test_exercise_two_3(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [13, 12, 3]
        hand.suits[Suits.HEART].cards = [14]
        hand.suits[Suits.DIAMOND].cards = [12, 8, 6, 4, 2]
        hand.suits[Suits.CLUB].cards = [13, 11, 6, 5]

        hand.evaluate()
        self.assertTrue(not hand.balanced)

    def test_exercise_two_4(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [13, 8]
        hand.suits[Suits.HEART].cards = [14, 13, 8, 6, 2]
        hand.suits[Suits.DIAMOND].cards = [13, 12, 7, 3]
        hand.suits[Suits.CLUB].cards = [9, 5]

        hand.evaluate()
        self.assertTrue(not hand.balanced)

    def test_exercise_two_5(self):
        hand = Hand(Positions.NORTH, {'use stayman': False})
        hand.suits[Suits.SPADE].cards = [13, 8]
        hand.suits[Suits.HEART].cards = [9, 5, 2]
        hand.suits[Suits.DIAMOND].cards = [14, 12, 8]
        hand.suits[Suits.CLUB].cards = [13, 12, 11, 7, 3]

        hand.evaluate()
        self.assertTrue(hand.balanced)

    def test_exercise_five_1(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [9, 6, 4]
        player.hand.suits[Suits.HEART].cards = [12, 11, 9, 8]
        player.hand.suits[Suits.DIAMOND].cards = [14, 13, 4]
        player.hand.suits[Suits.CLUB].cards = [14, 12, 11]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 17)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 17)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1nt')

    def test_exercise_five_2(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 11, 9, 8, 7]
        player.hand.suits[Suits.HEART].cards = [13, 7]
        player.hand.suits[Suits.DIAMOND].cards = [13, 11, 8, 2]
        player.hand.suits[Suits.CLUB].cards = [9, 8]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 12)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 13)
        bid = player.do_bid(self.bids, self.bid_table)
        # print("bid", bid.bid)
        self.assertTrue(bid.bid == '1s')

    def test_exercise_five_3(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [10, 9, 8]
        player.hand.suits[Suits.HEART].cards = [12, 9, 8, 7, 6]
        player.hand.suits[Suits.DIAMOND].cards = [14, 12, 11]
        player.hand.suits[Suits.CLUB].cards = [8, 5]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 9)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 10)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == 'p')

    def test_exercise_five_4(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [3]
        player.hand.suits[Suits.HEART].cards = [14, 11, 8, 6, 5]
        player.hand.suits[Suits.DIAMOND].cards = [13, 4]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 11, 7, 3]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 16)
        self.assertTrue(player.hand.distribution_points == 2)
        self.assertTrue(player.hand.dist == 18)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1h')

    def test_exercise_five_5(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 12, 7, 3]
        player.hand.suits[Suits.HEART].cards = [14, 9, 5]
        player.hand.suits[Suits.DIAMOND].cards = [7, 6]
        player.hand.suits[Suits.CLUB].cards = [13, 11, 6, 2]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 14)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 14)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1c')

    def test_exercise_five_6(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 11, 6, 3]
        player.hand.suits[Suits.HEART].cards = [5]
        player.hand.suits[Suits.DIAMOND].cards = [13, 11, 9, 4]
        player.hand.suits[Suits.CLUB].cards = [14, 8, 6, 2]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 13)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 13)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1d')

    def test_exercise_five_7(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [13, 4, 3]
        player.hand.suits[Suits.HEART].cards = [14, 13, 8, 6]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 5]
        player.hand.suits[Suits.CLUB].cards = [13, 11, 2]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 19)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 19)
        bid = player.do_bid(self.bids, self.bid_table)
        print("bid", bid.bid)
        self.assertTrue(bid.bid == '1c')

    def test_exercise_five_8(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [12, 8, 5, 3]
        player.hand.suits[Suits.HEART].cards = [12, 9, 6, 3]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 10]
        player.hand.suits[Suits.CLUB].cards = [14, 6]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 13)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 13)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1d')

    def test_exercise_five_9(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [4]
        player.hand.suits[Suits.HEART].cards = [14, 12, 9, 6, 3]
        player.hand.suits[Suits.DIAMOND].cards = [5]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 10, 7, 5, 2]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 13)
        self.assertTrue(player.hand.distribution_points == 3)
        self.assertTrue(player.hand.dist == 16)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1c')

    def test_example_1_page_37(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 12, 11, 4, 3]
        player.hand.suits[Suits.HEART].cards = [5, 3, 2]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 7]
        player.hand.suits[Suits.CLUB].cards = [11, 7]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 13)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 14)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1s')

    def test_example_2_page_37(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 2]
        player.hand.suits[Suits.HEART].cards = [13, 9, 8, 7, 3]
        player.hand.suits[Suits.DIAMOND].cards = [12, 11, 9, 8, 7]
        player.hand.suits[Suits.CLUB].cards = [14]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 14)
        self.assertTrue(player.hand.distribution_points == 2)
        self.assertTrue(player.hand.dist == 16)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1h')

    def test_example_3_page_37(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [9, 8]
        player.hand.suits[Suits.HEART].cards = [14, 13, 12]
        player.hand.suits[Suits.DIAMOND].cards = [13, 11, 10, 9]
        player.hand.suits[Suits.CLUB].cards = [11, 10, 9, 8]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 14)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 14)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1d')

    def test_example_4_page_37(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [13, 12, 3]
        player.hand.suits[Suits.HEART].cards = [9, 8, 7, 6, 3]
        player.hand.suits[Suits.DIAMOND].cards = [8, 4, 2]
        player.hand.suits[Suits.CLUB].cards = [10, 6]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 5)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 6)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == 'p')

    def test_example_1_page_38(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [12, 11, 10, 9]
        player.hand.suits[Suits.HEART].cards = [14, 9, 8]
        player.hand.suits[Suits.DIAMOND].cards = [12, 4, 3]
        player.hand.suits[Suits.CLUB].cards = [14, 9, 7]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 13)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 13)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1c')

    def test_example_2_page_38(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 9, 8, 7, 6]
        player.hand.suits[Suits.HEART].cards = [6]
        player.hand.suits[Suits.DIAMOND].cards = [4]
        player.hand.suits[Suits.CLUB].cards = [13, 12, 11, 9, 8, 3]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 10)
        self.assertTrue(player.hand.distribution_points == 3)
        self.assertTrue(player.hand.dist == 13)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1c')

    def test_example_1_bottom_page_38(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [11, 10, 9]
        player.hand.suits[Suits.HEART].cards = [14, 7, 6]
        player.hand.suits[Suits.DIAMOND].cards = [13, 8, 7, 2]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 11]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 16)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 16)
        self.assertTrue(player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1nt')

    def test_example_2_bottom_page_38(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [12, 9, 8, 7]
        player.hand.suits[Suits.HEART].cards = [13, 11]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 6, 2]
        player.hand.suits[Suits.CLUB].cards = [13, 12, 11]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 17)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 17)
        self.assertTrue(player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1nt')

    def test_example_3_bottom_page_38(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [11, 7, 3]
        player.hand.suits[Suits.HEART].cards = [14, 12, 9]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 10, 8, 5]
        player.hand.suits[Suits.CLUB].cards = [14, 9]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 16)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 17)
        self.assertTrue(player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1nt')

    def test_example_4_top_page_39(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [11, 10, 9]
        player.hand.suits[Suits.HEART].cards = [14, 7, 6]
        player.hand.suits[Suits.DIAMOND].cards = [9, 8, 7, 2]
        player.hand.suits[Suits.CLUB].cards = [14, 13, 11]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 13)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 13)
        self.assertTrue(player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1d')

    def test_example_5_top_page_39(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 12, 8, 7]
        player.hand.suits[Suits.HEART].cards = [13, 11]
        player.hand.suits[Suits.DIAMOND].cards = [14, 11, 6, 2]
        player.hand.suits[Suits.CLUB].cards = [13, 12, 11]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 21)
        self.assertTrue(player.hand.distribution_points == 0)
        self.assertTrue(player.hand.dist == 21)
        self.assertTrue(player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '2nt')

    def test_example_6_top_page_39(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [11]
        player.hand.suits[Suits.HEART].cards = [14, 12, 9, 3]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 10, 8, 5]
        player.hand.suits[Suits.CLUB].cards = [14, 11, 7]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 17)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 18)
        self.assertTrue(not player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1d')

    def test_example_6_top_page_39(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [11]
        player.hand.suits[Suits.HEART].cards = [14, 12, 9, 3]
        player.hand.suits[Suits.DIAMOND].cards = [13, 12, 10, 8, 5]
        player.hand.suits[Suits.CLUB].cards = [14, 11, 7]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 17)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 18)
        self.assertTrue(not player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1d')

    def test_bug_1(self):
        player = Player(Positions.NORTH)
        player.hand.suits[Suits.SPADE].cards = [14, 12, 11, 10, 9]
        player.hand.suits[Suits.HEART].cards = [13, 6, 2]
        player.hand.suits[Suits.DIAMOND].cards = [8, 7]
        player.hand.suits[Suits.CLUB].cards = [14, 12, 10]

        player.hand.evaluate()
        self.assertTrue(player.hand.hcp == 16)
        self.assertTrue(player.hand.distribution_points == 1)
        self.assertTrue(player.hand.dist == 17)
        self.assertTrue(player.hand.balanced)
        bid = player.do_bid(self.bids, self.bid_table)
        self.assertTrue(bid.bid == '1s')


if __name__ == '__main__':
    unittest.main()
    test_b1_c2 = TestBook1Chapter2()
