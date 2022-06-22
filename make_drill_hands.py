import logging
import pickle
import sys

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
    table_path = './bid_tables/acbl_series/' + table_name + '.json'
    bid_table = load_bid_table(table_path)

    drill_log.info("Starting program")

    drill_dict = {}
    practice_hands = []
    full_list = []

    last_length = 0
    last_length_count = 0
    need_more_practice_hands = True
    previous_bid = 'p'

    for row in bid_table:
        drill_dict[row["bid"]] = 0

    dealer = Positions.NORTH
    bids = BidStack(dealer)
    deck = Deck()

    while need_more_practice_hands:
        deck.reset()
        deck.shuffle()
        hands = deck.make_4_hands()

        for hand in hands:
            bids.reset(dealer)
            bids, hand = preload_bids(table_name, bids, hand)
            hand.evaluate()
            bid = bid_machine(hand, bids, bid_table)

            if bid.next_table in full_list:
                continue

            if drill_dict[bid.next_table] == 1000:
                full_list.append(bid.next_table)
                continue
            else:
                practice_hands.append(hand)
                drill_dict[bid.next_table] += 1

            if len(full_list) != last_length:
                last_length_count = 0
                last_length = len(full_list)
            else:
                last_length_count += 1

            if len(full_list) == len(drill_dict):
                need_more_practice_hands = False

            if last_length_count == 100000:
                need_more_practice_hands = False

    table_name = sys.argv[1]
    practice_hand_path = './practice_hands/' + table_name

    with open(practice_hand_path, "wb") as f:
        pickle.dump(practice_hands, f)



