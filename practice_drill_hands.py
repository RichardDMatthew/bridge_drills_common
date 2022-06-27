import logging
import pickle
import numpy as np
from bidding.bid_stack import BidStack, Positions
import pandas as pd
from bidding.bid_machine import bid_machine

if __name__ == '__main__':
    # set up logging
    PRACTICE_LOG_FILE = 'practice.log'
    open(PRACTICE_LOG_FILE, 'w')  # overwrites last log file
    practice_log = logging.getLogger(PRACTICE_LOG_FILE)
    practice_log.setLevel(logging.DEBUG)
    practice_log_file_handler = logging.FileHandler(PRACTICE_LOG_FILE)
    FORMAT = "[%(filename)s:%(lineno)s] %(funcName)5s() %(message)s"
    practice_log_file_handler.setFormatter(logging.Formatter(FORMAT))
    practice_log.addHandler(practice_log_file_handler)
    practice_log.info("Starting program")

    with open("./bidding/practice_hands/or2d", "rb") as f:  # Unpickling
        practice_hands = pickle.load(f)

    dealer = Positions.NORTH
    bids = BidStack(dealer)
    bid_table = pd.read_json('./bidding/bid_tables/acbl_series/or2d.json')
    hand_count = 0
    successful_bids = 0
    percent_success = 0
    np.random.shuffle(practice_hands)
    for hand in practice_hands:
        print('')
        hand_count += 1
        hand.evaluate()
        print('practice hand', hand_count)
        print('')
        hand.print()
        bid = bid_machine(hand, bids, bid_table)
        print('')
        guess = input('what is your bid? ')
        if guess == 'q':
            quit()
        if guess == bid.bid:
            successful_bids += 1

        else:
            print('\n----nope----')
            hand.print_description()
            print(bid.description)
            print(bid.reference)
            print(bid.comments)

        if successful_bids:
            percent_success = successful_bids / hand_count * 100
        print('percent success', int(percent_success))
        print('=================================')
