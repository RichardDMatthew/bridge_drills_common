import os
import pandas as pd

# from framework.bid_stack import Bid
from framework.bid_stack import get_candidate_bid_value
from bid_tables.acbl_series.or1_rules import or1_rules
from bid_tables.acbl_series.or2d_rules import or2d_rules
from bid_tables.acbl_series.or2e_rules import or2e_rules
from bid_tables.acbl_series.or2f_rules import or2f_rules
from bid_tables.acbl_series.or3a_rules import or3a_rules
from bid_tables.acbl_series.or3b_rules import or3b_rules
from bid_tables.acbl_series.or3c_rules import or3c_rules
from bid_tables.acbl_series.or3d_rules import or3d_rules
from bid_tables.acbl_series.or3f_rules import or3f_rules
from bid_tables.acbl_series.oyo_rules import oyo_rules
from cards.suit import Suits
import logging

practice_log = logging.getLogger('practice.log')


def bid_machine(hand, bids, bid_table):
    candidate_list = get_candidates(hand, bid_table, bids)
    index = bid_table.index
    bid = use_rules(bid_table.at[index.min(), "table id"], hand, bids, bid_table, candidate_list)
    return bid


def use_rules(table_id, hand, bids, bid_table, candidate_list):
    bid = None
    if table_id == 'or1':
        bid = or1_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or2d':
        bid = or2d_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or2e':
        bid = or2e_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or2f':
        bid = or2f_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or3a':
        bid = or3a_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or3b':
        bid = or3b_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or3c':
        bid = or3c_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or3d':
        bid = or3d_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'or3f':
        bid = or3f_rules(hand, bids, bid_table, candidate_list)
    elif table_id == 'oyo':
        bid = oyo_rules(hand, bids, bid_table, candidate_list)

    return bid


def get_candidates(hand, table, bids):
    candidate_list = []
    table.reset_index()
    highest_priority = 0    # priority filter
    # todo use this for dummy points
    partners_strain = bids.get_partners_strain(hand.position)
    my_bids = bids.get_my_bids(hand.position)
    if len(my_bids) > 0:
        my_opening_strain = my_bids[0].strain
        second_suit_filter = "not " + my_opening_strain
    else:
        my_opening_strain = None
        second_suit_filter = "post no bills"
    for index, row in table.iterrows():

        if partners_strain != row["supporting"] and "none" != row["supporting"] and \
                row["supporting"].find("not", 0, 3) == -1:
            # don't bother with bids that are for supporting a suit the bid isn't for
            continue
        if second_suit_filter == row["supporting"]:     # a way of filtering out non second suits
            continue
        practice_log.debug('index %s bid %s', index, row['bid'])
        points = 0
        good_shape = False

        # this filters out any bids that belong to a convention that isn't being used
        # if not hand.convention[row['convention']]:
        #     continue

        practice_log.debug('point type %s', row['point type'])
        if row['point type'] == "hcp":
            points = hand.hcp
        elif row['point type'] == 'dist':
            points = hand.dist
        elif row['point type'] == 'any':
            points = hand.dist
        elif row['point type'] == 'dummy':
            hand.set_dummy_points(partners_strain)
            points = hand.dummy_points
        else:
            practice_log.error('incorrect point type index %s point type %s', index, row['point type'])

        if not row["minimum points"] <= points <= row['maximum points']:
            practice_log.debug('min %s points %s max %s', row["minimum points"], points, row['maximum points'])
            continue

        if row["shape"] == hand.shape:
            good_shape = True
        elif row["shape"] == 'any':
            good_shape = True
        elif row["shape"] == 'skew' and hand.shape == 'bal':
            good_shape = True
        if not good_shape:
            practice_log.debug('row shape %s hand shape %s', row["shape"], hand.shape)
            continue

        if hand.stopped_suits < row["stopped suits"]:
            practice_log.debug('stopped suits %s hand.stopped_suits %s', row["stopped suits"], hand.stopped_suits)
            continue

        if partners_strain is not None and partners_strain != 'no trump':
            stoppers = hand.stoppers_in_other_suits(partners_strain)
            if stoppers < row["stopped other suits"]:
                practice_log.debug('stopped other suits % stoppers %', row["stopped other suits"], stoppers)
                continue

        if partners_strain == row["supporting"] and hand.suits[Suits.CLUB].length < row["c length"]:
            practice_log.debug('c length %s club length %s', row["c length"], hand.suits[Suits.CLUB].length)
            continue
        elif hand.suits[Suits.CLUB].length < row["c length"]:
            practice_log.debug('c length %s club length %s', row["c length"], hand.suits[Suits.CLUB].length)
            continue

        if hand.suits[Suits.CLUB].protected_honors < row["c protected honors"]:
            practice_log.debug('c protected honors %s protected honors %s',
                               row["c protected honors"], hand.suits[Suits.CLUB].protected_honors)
            continue

        if hand.suits[Suits.CLUB].high_honors < row["c high honors"]:
            practice_log.debug('c high honors %s high honors %s', row["c high honors"],
                               hand.suits[Suits.CLUB].high_honors)
            continue

        if partners_strain == row["supporting"] and hand.suits[Suits.DIAMOND].length < row["d length"]:
            practice_log.debug('d length %s diamond length %s', row["d length"], hand.suits[Suits.DIAMOND].length)
            continue
        elif hand.suits[Suits.DIAMOND].length < row["d length"]:
            practice_log.debug('d length %s diamond length %s', row["d length"], hand.suits[Suits.DIAMOND].length)
            continue

        if hand.suits[Suits.DIAMOND].protected_honors < row["d protected honors"]:
            practice_log.debug('d protected honors %s protected honors %s', row["d protected honors"],
                               hand.suits[Suits.DIAMOND].protected_honors)
            continue

        if hand.suits[Suits.DIAMOND].high_honors < row["d high honors"]:
            practice_log.debug('d high honors %s high honors %s', row["d high honors"],
                               hand.suits[Suits.DIAMOND].high_honors)
            continue

        if partners_strain == row["supporting"] and hand.suits[Suits.HEART].length < row["h length"]:
            practice_log.debug('h length %s heart length %s', row["h length"], hand.suits[Suits.HEART].length)
            continue
        elif hand.suits[Suits.HEART].length < row["h length"]:
            practice_log.debug('h length %s heart length %s', row["h length"], hand.suits[Suits.HEART].length)
            continue

        if hand.suits[Suits.HEART].protected_honors < row["h protected honors"]:
            practice_log.debug('h protected honors %s protected honors %s', row["h protected honors"],
                               hand.suits[Suits.HEART].protected_honors)
            continue

        if hand.suits[Suits.HEART].high_honors < row["h high honors"]:
            practice_log.debug('h high honors %s high honors %s', row["h high honors"],
                               hand.suits[Suits.HEART].high_honors)
            continue

        if partners_strain == row["supporting"] and hand.suits[Suits.SPADE].length < row["s length"]:
            practice_log.debug('s length %s spade length %s', row["s length"], hand.suits[Suits.SPADE].length)
            continue
        elif hand.suits[Suits.SPADE].length < row["s length"]:
            practice_log.debug('s length %s spade length %s', row["s length"], hand.suits[Suits.SPADE].length)
            continue

        if hand.suits[Suits.SPADE].protected_honors < row["s protected honors"]:
            practice_log.debug('s protected honors %s protected honors %s', row["s protected honors"],
                               hand.suits[Suits.SPADE].protected_honors)
            continue

        if hand.suits[Suits.SPADE].high_honors < row["s high honors"]:
            practice_log.debug('s high honors %s high honors %s', row["s high honors"],
                               hand.suits[Suits.SPADE].high_honors)
            continue

        # don't add pass to candidate list if there is a qualifying bid
        if len(candidate_list) >= 1 and row["bid"] == 'p':
            continue

        candidate_list.append(index)

    # bid level filter
    last_bid_value = bids.get_last_bid_value()
    for candidate in candidate_list:
        if table.at[candidate, 'level'] == 0:
            continue
        candidate_bid_value = get_candidate_bid_value(table.at[candidate, 'level'], table.at[candidate, 'strain'])
        if candidate_bid_value <= last_bid_value:
            candidate_list.remove(candidate)

    # get rid of lower priority bids
    for candidate in candidate_list:
        blah = table.at[candidate, 'priority']
        if table.at[candidate, 'priority'] > highest_priority:
            highest_priority = table.at[candidate, 'priority']

    # priority filter
    complete = False
    while not complete:
        complete = True
        for candidate in candidate_list:
            if table.at[candidate, 'priority'] < highest_priority:
                candidate_list.remove(candidate)
                complete = False

    return candidate_list


def load_bid_table(directory):
    dfs = []
    files = os.listdir(directory)
    for filename in files:
        split_filename = filename.split('.')
        if filename == '__pycache__' or split_filename[1] == 'txt' or split_filename[1] == 'py':
            continue
        filepath = directory + filename
        # print(filepath)
        data = pd.read_json(filepath)
        dfs.append(data)

    framework_table_df = pd.concat(dfs, ignore_index=True)
    framework_table_df.to_csv('bid_table.csv')

    return framework_table_df
