import logging
import pickle
import numpy as np
from bidding.bid_stack import BidStack, Positions
import pandas as pd
from bidding.bid_machine import bid_machine

legal_bids = ['p',
              '1c', '1d', '1h', '1s', '1nt',
              '2c', '2d', '2h', '2s', '2nt',
              '3c', '3d', '3h', '3s', '3nt',
              '4c', '4d', '4h', '4s', '4nt',
              '5c', '5d', '5h', '5s', '5nt',
              '6c', '6d', '6h', '6s', '6nt',
              '7c', '7d', '7h', '7s', '7nt', ]


def legal_bid(bid):
    if bid in legal_bids:
        return True
    else:
        return False


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
    print()
    print('enter the number of the bids you want to practice')
    print('--------------------------------------')
    print('1. opening')
    print('2. responding to 1 no trump opening')
    print('3. responding to 1 major suit opening')
    print('4. responding to 1 minor suit opening')
    print('--------------------------------------')
    selection = input('what would you like to practice? ')
    print()
    if selection == '1':
        table_name = 'or1'
        print('opening bid')
    elif selection == '2':
        table_name = 'or2d'
        print('responding to 1 no trump opening')
    elif selection == '3':
        table_name = 'or2e'
        print('responding to 1 major suit opening')
    elif selection == '4':
        table_name = 'or2r'
        print('responding to 1 minor suit opening')

    filename = './bidding/practice_hands/' + table_name
    with open(filename, "rb") as f:  # Unpickling
        practice_hands = pickle.load(f)

    dealer = Positions.NORTH
    bids = BidStack(dealer)
    filename = './bidding/bid_tables/acbl_series/' + table_name + '.json'
    bid_table = pd.read_json(filename)
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
        while not legal_bid(guess):
            print('legal bids are 1c, 1d, 1h, 1s, 1nt up to 7nt - q to quit')
            guess = input('try again ')
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
