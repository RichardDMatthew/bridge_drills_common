import logging

# from bidding.bid_stack import print_bid
from bidding.bid_stack import get_right_opponent, get_partner

from player import Player
from bidding.bid_stack import Positions
from cards.suit import Suits
from players.players import get_next_player
# from practice import Practice

log = logging.getLogger('Bridge')


class Players:
    def __init__(self):
        self.players = [Player(position) for position in Positions]
        self.hand_data = [HandData(position) for position in Positions]
        # todo: is there a way to move practice out of players?
        # self.practice = Practice()
        self.ns_points = 0
        self.ew_points = 0

    def reset(self):
        for player in self.players:
            player.reset()

        for hand_data in self.hand_data:
            hand_data.reset()

    def organize_hands(self):
        for player in self.players:
            player.organize_hand()

    # players bid until there are three sequential passes
    def do_auction(self, bids, bid_table):
        bid_opened = False
        bidder = bids.dealer
        # do until passed_out which is handled in do_bid()
        loop_counter = 1
        while True:
            loop_counter += 1
            bid = self.players[bidder].do_bid(bids, bid_table)

            # on opening bid set up opponents with overcaller/advancer bid tables
            if not bid_opened and bid.level > 0:
                bid_opened = True
                right_hand_opponent = get_right_opponent(bidder)
                self.players[right_hand_opponent].next_table = 'oa1'
                opponents_partner = get_partner(right_hand_opponent)
                self.players[opponents_partner].next_table = 'oa1'

            bidders_partner = get_partner(bidder)
            self.players[bidders_partner].next_table = bid.next_table

            self.show_hands(bids)
            passed_out = bids.push(bid)
            # hand = self.players[bidder].hand
            # finished = self.practice.bidding_practice(hand, bids, bid_table)
            # finished = True
            # if finished:
            #     passed_out = True
            if passed_out:
                # bypass all other bidding and exit loop
                break
            bidder = get_next_player(bidder)
        return finished     # if finished is true then a hand was practiced

    # todo: fill this in
    def find_winning_play(self, contract, plays):
        return Positions.NORTH

    # todo: fill this in
    def count_tricks(self, contract, tricks):
        return 0

    # todo: fill this in
    def count_points(self, contract, tricks):
        return 100, 0

    def do_play(self, contract):
        tricks = []
        player = get_next_player(contract.bidder)
        for trick in range(13):
            plays = []
            for _ in range(4):
                plays.append(self.players[player].do_play())
                player = get_next_player(player)
            winner = self.find_winning_play(contract, plays)
            tricks.append(winner)
            player = winner
        over_under = self.count_tricks(contract, tricks)
        ns_points, ew_points = self.count_points(contract, over_under)
        self.ns_points += ns_points
        self.ew_points += ew_points

    def review_bidding(self, bids):

        for bid in bids.stack:
            self.hand_data[bid.bidder].reset()

        for bid in bids.stack:
            self.hand_data[bid.bidder].add_info(bids, bid)

    def generate_strategy(self, bids):
        pass

    def show_hands(self, bids):
        # print position
        print('=======================================================================================================')
        print('\t\t\t\t\t\t\t{:<58}'.format('NORTH'))

        # print out hand
        for suit in reversed(Suits):
            print('\t\t\t\t\t\t\t{:<62}'.format(self.players[Positions.NORTH].hand.suits[suit].list()))
        print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))

        # print out total points and balanced or not
        if self.players[Positions.NORTH].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'
        tmp_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                              str(self.players[Positions.NORTH].hand.high_card_points),
                                                              str(self.players[
                                                                      Positions.NORTH].hand.distribution_points),
                                                              str(self.players[Positions.NORTH].hand.dummy_points))

        # print out bidding
        print('\t\t\t\t\t\t\t{:<58}'.format(tmp_string))
        print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))
        # index = bids.get_first_index_of(Positions.NORTH, bids)
        # while index < bids.size():
        #     bid = bids.read(index)
        #     if bid.bid_type == common.BidType.PASS:
        #         tmp_string = '{0}: {1} {2}'.format(str(index), str(bid.bid_type.name), str(bid.message.name))
        #     else:
        #         tmp_string = '{0}: {1} {2} {3} {4}'.format(str(index), str(bid.bid_type.name), str(bid.level),
        #                                                    str(bid.strain.name), str(bid.message.name))
        #     print('\t\t\t\t\t\t\t{:<42}'.format(tmp_string))
        #     if bid.bid_type != common.BidType.PASS:
        #         print('\t\t\t\t\t\t\t{:<42}'.format(commentary.show_meaning(bid)))
        #     print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))
        #     index += 4
        # print()

        # ------------------------------------
        # for printing west and east hands
        # ------------------------------------
        tmp_string = '{:85}'.format('WEST')
        tmp_string += '{:85}'.format('EAST')
        print(tmp_string)
        for suit in reversed(Suits):
            tmp_string = '{:<85}'.format(self.players[Positions.WEST].hand.suits[suit].list())
            tmp_string += '{:<85}'.format(self.players[Positions.EAST].hand.suits[suit].list())
            print(tmp_string)

        tmp_string = '{:<85}'.format('------------------------')
        tmp_string += '{:<85}'.format('------------------------')
        print(tmp_string)

        if self.players[Positions.WEST].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'

        west_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                               str(self.players[Positions.WEST].hand.high_card_points),
                                                               str(self.players[
                                                                       Positions.WEST].hand.distribution_points),
                                                               str(self.players[Positions.WEST].hand.dummy_points))

        if self.players[Positions.EAST].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'

        east_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                               str(self.players[Positions.EAST].hand.high_card_points),
                                                               str(self.players[
                                                                       Positions.EAST].hand.distribution_points),
                                                               str(self.players[Positions.EAST].hand.dummy_points))

        tmp_string = '{:<85}'.format(west_string)
        tmp_string += '{:<85}'.format(east_string)

        print(tmp_string)

        tmp_string = '{:<85}'.format('------------------------')
        tmp_string += '{:<85}'.format('------------------------')
        print(tmp_string)

        # east_index = bids.get_first_index_of(Positions.EAST)
        # west_index = bids.get_first_index_of(Positions.WEST)
        #
        # while east_index < bids.size() or west_index < bids.size():
        #     west_passed = False
        #     east_passed = False
        #     if west_index >= bids.size():
        #         west_string = ''
        #         west_passed = True
        #     else:
        #         bid = bids.read(west_index)
        #         if bid.bid_type == common.BidType.PASS:
        #             west_passed = True
        #             west_string = '{0}: {1} {2}'.format(str(west_index), str(bid.bid_type.name),
        #                                                 str(bid.message.name))
        #         else:
        #             west_string = '{0}: {1} {2} {3} {4}'.format(str(west_index),
        #                                                         str(bid.bid_type.name), str(bid.level),
        #                                                         str(bid.strain.name), str(bid.message.name))
        #     tmp_string = '{:<85}'.format(west_string)
        #     if bid.bid_type == common.BidType.PASS:
        #         tmp_comment = '{:<85}'.format('')
        #     else:
        #         tmp_comment = '{:<85}'.format(commentary.show_meaning(bid))
        #
        #     west_index += 4
        #
        #     if east_index >= bids.size():
        #         east_string = ''
        #         east_passed = True
        #     else:
        #         bid = bids.read(east_index)
        #         if bid.bid_type == common.BidType.PASS:
        #             east_passed = True
        #             east_string = '{0}: {1} {2}'.format(str(east_index), str(bid.bid_type.name),
        #                                                 str(bid.message.name))
        #         else:
        #             east_string = '{0}: {1} {2} {3} {4}'. \
        #                 format(str(east_index), str(bid.bid_type.name), str(bid.level),
        #                        str(bid.strain.name), str(bid.message.name))
        #     tmp_string += '{:<85}'.format(east_string)
        #     if bid.bid_type == common.BidType.PASS:
        #         tmp_comment += '{:<85}'.format('')
        #     else:
        #         tmp_comment += '{:<85}'.format(commentary.show_meaning(bid))
        #     east_index += 4
        #
        #     print(tmp_string)
        #     if not west_passed or not east_passed:
        #         print(tmp_comment)
        #     tmp_string = '{:<85}'.format('------------------------')
        #     tmp_string += '{:<85}'.format('------------------------')
        #     print(tmp_string)
        # print('')

        # ---------------------------------------
        # for printing south hand
        # ---------------------------------------
        print('\t\t\t\t\t\t\t{:<42}'.format('SOUTH'))
        for suit in reversed(Suits):
            print('\t\t\t\t\t\t\t{:<42}'.format(self.players[Positions.SOUTH].hand.suits[suit].list()))

        print('\t\t\t\t\t\t\t{:<42}'.format('---------------------'))

        if self.players[Positions.SOUTH].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'

        tmp_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                              str(self.players[Positions.SOUTH].hand.high_card_points),
                                                              str(self.players[
                                                                      Positions.SOUTH].hand.distribution_points),
                                                              str(self.players[Positions.SOUTH].hand.dummy_points))

        print('\t\t\t\t\t\t\t{:<42}'.format(tmp_string))

        print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))
        # index = bids.get_first_index_of(Positions.SOUTH)
        # while index < bids.size():
        #     bid = bids.read(index)
        #     if bid.bid_type == common.BidType.PASS:
        #         tmp_string = '{0}: {1} {2}'.format(str(index), str(bid.bid_type.name), str(bid.message.name))
        #     else:
        #         tmp_string = '{0}: {1} {2} {3} {4}'.format(str(index), str(bid.bid_type.name), str(bid.level),
        #                                                    str(bid.strain.name), str(bid.message.name))
        #     print('\t\t\t\t\t\t\t{:<58}'.format(tmp_string))
        #     if bid.bid_type != common.BidType.PASS:
        #         print('\t\t\t\t\t\t\t{:<58}'.format(commentary.show_meaning(bid)))
        #     print('\t\t\t\t\t\t\t{:<42}'.format('---------------------'))
        #
        #     index += 4
        # print()

    def show_hands_data(self, bids):
        # print position
        print('=======================================================================================================')
        print('\t\t\t\t\t\t\t{:<58}'.format('NORTH'))

        # print out hand
        for suit in reversed(Suits):
            print('\t\t\t\t\t\t\t{} {:<62}'.format(self.hand_data[Positions.NORTH].suits[suit].length.min,
                                                   self.hand_data[Positions.NORTH].suits[suit].length.max))
        print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))

        # print out total points and balanced or not
        if self.players[Positions.NORTH].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'
        tmp_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                              str(self.players[Positions.NORTH].hand.high_card_points),
                                                              str(self.players[
                                                                      Positions.NORTH].hand.distribution_points),
                                                              str(self.players[Positions.NORTH].hand.dummy_points))

        # print out bidding
        print('\t\t\t\t\t\t\t{:<58}'.format(tmp_string))
        print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))
        index = bids.get_first_index_of(Positions.NORTH)
        while index < bids.size():
            bid = bids.read(index)
            if bid.bid_type == common.BidType.PASS:
                tmp_string = '{0}: {1} {2}'.format(str(index), str(bid.bid_type.name), str(bid.message.name))
            else:
                tmp_string = '{0}: {1} {2} {3} {4}'.format(str(index), str(bid.bid_type.name), str(bid.level),
                                                           str(bid.strain.name), str(bid.message.name))
            print('\t\t\t\t\t\t\t{:<42}'.format(tmp_string))
            if bid.bid_type != common.BidType.PASS:
                print('\t\t\t\t\t\t\t{:<42}'.format(commentary.show_meaning(bid)))
            print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))
            index += 4
        print()

        # ------------------------------------
        # for printing west and east hands
        # ------------------------------------
        tmp_string = '{:85}'.format('WEST')
        tmp_string += '{:85}'.format('EAST')
        print(tmp_string)
        for suit in reversed(Suits):
            tmp_string = '{} {:<85}'.format(self.hand_data[Positions.WEST].suits[suit].length.min,
                                            self.hand_data[Positions.WEST].suits[suit].length.max)
            tmp_string += '{} {:<85}'.format(self.hand_data[Positions.EAST].suits[suit].length.min,
                                             self.hand_data[Positions.EAST].suits[suit].length.max)
            print(tmp_string)

        tmp_string = '{:<85}'.format('------------------------')
        tmp_string += '{:<85}'.format('------------------------')
        print(tmp_string)

        if self.players[Positions.WEST].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'

        west_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                               str(self.players[Positions.WEST].hand.high_card_points),
                                                               str(self.players[
                                                                       Positions.WEST].hand.distribution_points),
                                                               str(self.players[Positions.WEST].hand.dummy_points))

        if self.players[Positions.EAST].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'

        east_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                               str(self.players[Positions.EAST].hand.high_card_points),
                                                               str(self.players[
                                                                       Positions.EAST].hand.distribution_points),
                                                               str(self.players[Positions.EAST].hand.dummy_points))

        tmp_string = '{:<85}'.format(west_string)
        tmp_string += '{:<85}'.format(east_string)

        print(tmp_string)

        tmp_string = '{:<85}'.format('------------------------')
        tmp_string += '{:<85}'.format('------------------------')
        print(tmp_string)

        east_index = bids.get_first_index_of(Positions.EAST)
        west_index = bids.get_first_index_of(Positions.WEST)

        while east_index < bids.size() or west_index < bids.size():
            west_passed = False
            east_passed = False
            if west_index >= bids.size():
                west_string = ''
                west_passed = True
            else:
                bid = bids.read(west_index)
                if bid.bid_type == common.BidType.PASS:
                    west_passed = True
                    west_string = '{0}: {1} {2}'.format(str(west_index), str(bid.bid_type.name),
                                                        str(bid.message.name))
                else:
                    west_string = '{0}: {1} {2} {3} {4}'.format(str(west_index),
                                                                str(bid.bid_type.name), str(bid.level),
                                                                str(bid.strain.name), str(bid.message.name))
            tmp_string = '{:<85}'.format(west_string)
            if bid.bid_type == common.BidType.PASS:
                tmp_comment = '{:<85}'.format('')
            else:
                tmp_comment = '{:<85}'.format(commentary.show_meaning(bid))

            west_index += 4

            if east_index >= bids.size():
                east_string = ''
                east_passed = True
            else:
                bid = bids.read(east_index)
                if bid.bid_type == common.BidType.PASS:
                    east_passed = True
                    east_string = '{0}: {1} {2}'.format(str(east_index), str(bid.bid_type.name),
                                                        str(bid.message.name))
                else:
                    east_string = '{0}: {1} {2} {3} {4}'. \
                        format(str(east_index), str(bid.bid_type.name), str(bid.level),
                               str(bid.strain.name), str(bid.message.name))
            tmp_string += '{:<85}'.format(east_string)
            if bid.bid_type == common.BidType.PASS:
                tmp_comment += '{:<85}'.format('')
            else:
                tmp_comment += '{:<85}'.format(commentary.show_meaning(bid))
            east_index += 4

            print(tmp_string)
            if not west_passed or not east_passed:
                print(tmp_comment)
            tmp_string = '{:<85}'.format('------------------------')
            tmp_string += '{:<85}'.format('------------------------')
            print(tmp_string)
        print('')

        # ---------------------------------------
        # for printing south hand
        # ---------------------------------------
        print('\t\t\t\t\t\t\t{:<42}'.format('SOUTH'))
        for suit in reversed(Suits):
            print('\t\t\t\t\t\t\t{} {:<42}'.format(self.hand_data[Positions.SOUTH].suits[suit].length.min,
                                                   self.hand_data[Positions.SOUTH].suits[suit].length.max))

        print('\t\t\t\t\t\t\t{:<42}'.format('---------------------'))

        if self.players[Positions.SOUTH].hand.balanced:
            balanced_string = 'balanced'
        else:
            balanced_string = 'not balanced'

        tmp_string = '{0} {1}  HCP {2} dist {3} dummy'.format(balanced_string,
                                                              str(self.players[Positions.SOUTH].hand.high_card_points),
                                                              str(self.players[
                                                                      Positions.SOUTH].hand.distribution_points),
                                                              str(self.players[Positions.SOUTH].hand.dummy_points))

        print('\t\t\t\t\t\t\t{:<42}'.format(tmp_string))

        print('\t\t\t\t\t\t\t{:<58}'.format('---------------------'))
        index = bids.get_first_index_of(Positions.SOUTH)
        while index < bids.size():
            bid = bids.read(index)
            if bid.bid_type == common.BidType.PASS:
                tmp_string = '{0}: {1} {2}'.format(str(index), str(bid.bid_type.name), str(bid.message.name))
            else:
                tmp_string = '{0}: {1} {2} {3} {4}'.format(str(index), str(bid.bid_type.name), str(bid.level),
                                                           str(bid.strain.name), str(bid.message.name))
            print('\t\t\t\t\t\t\t{:<58}'.format(tmp_string))
            if bid.bid_type != common.BidType.PASS:
                print('\t\t\t\t\t\t\t{:<58}'.format(commentary.show_meaning(bid)))
            print('\t\t\t\t\t\t\t{:<42}'.format('---------------------'))

            index += 4
        print()

    def get_first_bid_of(self, bidder):
        for bid in self.stack:
            if not bid.state == common.BidState.DEALT:
                if bid.bidder == bidder:
                    return bid
        return None


