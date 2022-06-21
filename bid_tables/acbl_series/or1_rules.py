# with 15-17 HCP and a balanced hand, which has priority, a 5 card major or no trump?
from framework.bid_stack import Bid
from cards.suit import Strains, Suits


def or1_rules(hand, bids, bid_table, candidate_list):
    suit_len_dict = {'spades': len(hand.suits[Suits.SPADE].cards), 'hearts': len(hand.suits[Suits.HEART].cards),
                     'diamonds': len(hand.suits[Suits.DIAMOND].cards), 'clubs': len(hand.suits[Suits.CLUB].cards)}
    # print(suit_len_dict)

    no_trump = False
    majors = False
    minors = False
    minor_length = 0
    spades = False
    diamonds = False
    longest_length = 0

    # if there are the same bid on different levels remove the lower one
    # clubs
    if 11 in candidate_list and 15 in candidate_list:
        candidate_list.remove(15)

    # diamonds
    if 10 in candidate_list and 14 in candidate_list:
        candidate_list.remove(14)
    if 10 in candidate_list and 18 in candidate_list:
        candidate_list.remove(18)
    if 14 in candidate_list and 18 in candidate_list:
        candidate_list.remove(18)

    # hearts
    if 9 in candidate_list and 13 in candidate_list:
        candidate_list.remove(13)
    if 9 in candidate_list and 17 in candidate_list:
        candidate_list.remove(17)
    if 13 in candidate_list and 17 in candidate_list:
        candidate_list.remove(17)

    # spades
    if 8 in candidate_list and 12 in candidate_list:
        candidate_list.remove(12)
    if 8 in candidate_list and 16 in candidate_list:
        candidate_list.remove(16)
    if 12 in candidate_list and 16 in candidate_list:
        candidate_list.remove(16)

    # if there is a 1nt bid and a 5 card major, if the major is strong use it, otherwise use no trump
    one_no_trump = False
    for index in candidate_list:
        if bid_table.at[index, 'bid'] == '1nt':
            one_no_trump = True

    if one_no_trump:
        while len(candidate_list) > 1:
            for index in candidate_list:
                if bid_table.at[index, 'bid'] == '1nt':
                    continue
                elif bid_table.at[index, 'bid'] == '1s':
                    candidate_list = [index]
                    break
                elif bid_table.at[index, 'bid'] == '1h':
                    candidate_list = [index]
                    break
                else:
                    candidate_list.remove(index)

    # look to see if there is a no trump bid - prefers no trump over suit
    for index in candidate_list:
        if bid_table.at[index, 'bid'] == '2nt' or bid_table.at[index, 'bid'] == '3nt':
            candidate_list = [index]
            break

    # it's a suit bid or pass
    last_length = 100
    while len(candidate_list) > 1:
        if last_length == len(candidate_list):
            blah = 0
        last_length = len(candidate_list)
        # print("length of candidate list", len(candidate_list))
        # print(candidate_list)
        # look for longest suit(s)
        for index in candidate_list:
            # find longest bid suit
            if suit_len_dict[bid_table.at[index, 'strain']] > longest_length:
                longest_length = suit_len_dict[bid_table.at[index, 'strain']]

        # remove anything shorter
        for index in candidate_list:
            if suit_len_dict[bid_table.at[index, 'strain']] < longest_length:
                candidate_list.remove(index)

        # major preferred over minor
        for index in candidate_list:
            if bid_table.at[index, 'strain'] == 'spades' or bid_table.at[index, 'strain'] == 'hearts':
                majors = True
                if bid_table.at[index, 'strain'] == 'spades':
                    spades = True
            else:
                minors = True
                if bid_table.at[index, 'strain'] == 'diamonds':
                    diamonds = True

        if majors:
            minors = False

        for index in candidate_list:
            if majors:
                if bid_table.at[index, 'strain'] == 'diamonds' or bid_table.at[index, 'strain'] == 'clubs':
                    candidate_list.remove(index)
                elif spades and bid_table.at[index, 'strain'] == 'hearts':
                    candidate_list.remove(index)
            elif minors:    # could be a pass
                if suit_len_dict[bid_table.at[index, 'strain']] > minor_length:
                    minor_length = suit_len_dict[bid_table.at[index, 'strain']]

        for index in candidate_list:
            if minors:
                if bid_table.at[index, 'strain'] == 'diamonds':
                    if suit_len_dict['diamonds'] < suit_len_dict['clubs']:
                        candidate_list.remove(index)
                        break
                    elif suit_len_dict['diamonds'] == suit_len_dict['clubs']:
                        if suit_len_dict['diamonds'] <= 3:
                            candidate_list.remove(index)
                            break
                elif bid_table.at[index, 'strain'] == 'clubs':
                    if suit_len_dict['clubs'] < suit_len_dict['diamonds']:
                        candidate_list.remove(index)
                        break
                    elif suit_len_dict['clubs'] == suit_len_dict['diamonds']:
                        if suit_len_dict['clubs'] > 3:
                            candidate_list.remove(index)
                            break

    index = candidate_list[0]
    # bridge_log.debug('table id %s bid %s', bid_table.at[index, "table id"], bid_table.at[index, "bid"])
    bid = Bid(hand.position,
              table_id=bid_table.at[index, "table id"],
              bid=bid_table.at[index, "bid"],
              level=bid_table.at[index, "level"],
              strain=bid_table.at[index, "strain"],
              next_table=bid_table.at[index, "next table"],
              description=bid_table.at[index, "description"],
              reference=bid_table.at[index, "reference"],
              comments=bid_table.at[index, "comments"])
    return bid
