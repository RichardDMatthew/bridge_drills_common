import logging
import pickle
import sys
import pandas as pd

from bidding.bid_machine import bid_machine
from bidding.bid_stack import BidStack, Positions
from bidding.preload_bids import preload_bids
from cards import deck
from bidding.bid_machine import load_bid_table
from cards.deck import Deck

if __name__ == '__main__':
    DRILL_LOG = 'drill.log'
    open(DRILL_LOG, 'w')  # overwrites last log file
    drill_log = logging.getLogger(DRILL_LOG)
    drill_log.setLevel(logging.DEBUG)
    drill_log_file_handler = logging.FileHandler(DRILL_LOG)
    FORMAT = "[%(filename)s:%(lineno)s] %(funcName)5s() %(message)s"
    drill_log_file_handler.setFormatter(logging.Formatter(FORMAT))
    drill_log.addHandler(drill_log_file_handler)

    table_name = sys.argv[1]
    # table_path = './bidding/bid_tables/acbl_series/' + table_name + '.json'
    bid_table = load_bid_table('./bidding/bid_tables/acbl_series/')
    # bid_table = pd.read_json(table_path)
    drill_log.info("Starting program")

    drill_dict = {}
    practice_hands = []
    full_list = []

    last_length = 0
    last_length_count = 0
    need_more_practice_hands = True
    previous_bid = 'p'
    count_since_hand_added = 0

    dealer = Positions.NORTH
    bids = BidStack(dealer)
    deck = Deck()

    opener_table = bid_table[bid_table["table id"] == 'or1']
    responder_table = bid_table[bid_table["table id"] == table_name]
    for index, row in responder_table.iterrows():
        drill_dict[row["bid"]] = 0

    while need_more_practice_hands:
        # print('need_more_practice_hands')
        deck.reset()
        deck.shuffle()
        hands = deck.make_4_hands()
        hand_set = hands * 2
        # hand_set is [hand_1, hand_2, hand_3, hand_4, hand_1, hand_2, hand_3, hand_4]
        # the idea is if I start with [0] and it's a 1 nt bid, then I can get [2] as a sample hand
        # then go on to [1] and [3], [2] and [4], [3] and [5]
        # using this scheme I can maximize the number of test hands I can use out of each shuffle.
        hand_num = 0
        while hand_num != 4:
            # print('while hand_num', hand_num)
            count_since_hand_added += 1
            hand = hand_set[hand_num]
            hand.evaluate()
            # hand.print()
            bid = bid_machine(hand, bids, opener_table)
            if bid.bid == '1nt':
                # print('if bid.bid')
                hand = hand_set[hand_num + 2]   # responder's hand
                hand.evaluate()
                bid = bid_machine(hand, bids, responder_table)
                if bid.bid in full_list:
                    hand_num += 1
                    continue

                if drill_dict[bid.bid] == 1000:
                    full_list.append(bid.bid)
                    hand_num += 1
                    continue
                else:
                    practice_hands.append(hand)
                    drill_dict[bid.bid] += 1
                    print(count_since_hand_added, drill_dict)
                    count_since_hand_added = 0
            hand_num += 1

        if count_since_hand_added >= 10000:
            need_more_practice_hands = False
            # print('done because of high count')

        if len(full_list) == len(drill_dict):
            need_more_practice_hands = False
            # print('done because of full list')
            # print(full_list)


        # print(drill_dict)
    table_name = sys.argv[1]
    practice_hand_path = './bidding/practice_hands/' + table_name

    with open(practice_hand_path, "wb") as f:
        pickle.dump(practice_hands, f)



