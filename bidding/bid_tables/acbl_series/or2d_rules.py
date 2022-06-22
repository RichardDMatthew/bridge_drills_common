from bidding.bid_stack import Bid


def or2d_rules(hand, bids, bid_table, candidate_list):

    majors_bid = False
    for index in candidate_list:
        if bid_table.at[index, 'bid'] == '4s' or bid_table.at[index, 'bid'] == '4h' or \
                bid_table.at[index, 'bid'] == '3s' or bid_table.at[index, 'bid'] == '3h':
            majors_bid = True

    for index in candidate_list:
        if bid_table.at[index, 'bid'] == '3nt' and majors_bid:
            candidate_list.remove(index)
            break

    if len(candidate_list) == 0:
        blah = len(candidate_list)
    index = candidate_list[0]
    # bridge_log.debug('table id %s bid %s', bid_table.at[index, "table id"], bid_table.at[index, "bid"])

    bid = Bid(hand.position,
              table_id=bid_table.at[index, "table id"],
              bid=bid_table.at[index, "bid"],
              level=bid_table.at[index, "level"],
              strain=bid_table.at[index, "strain"],
              next_table=bid_table.at[index, 'next table'],
              description=bid_table.at[index, "description"],
              reference=bid_table.at[index, "reference"],
              comments=bid_table.at[index, "comments"])
    return bid
