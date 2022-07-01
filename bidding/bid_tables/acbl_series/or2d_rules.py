from bidding.bid_stack import Bid
from cards.suit import Suits


def or2d_rules(hand, bids, bid_table, candidate_list):

    index_list = bid_table.index
    table_offset = index_list[0]

    while len(candidate_list) > 1:
        lowest_candidate = 999
        for candidate in candidate_list:
            if candidate < lowest_candidate:
                lowest_candidate = candidate

        list_index = 0
        for candidate_index in candidate_list:
            # print(candidate_index)
            # if list_index > 0:
                # print(list_index, candidate_index, candidate_list)
            # bid_num = candidate_index - table_offset
            priority = bid_table.at[candidate_list[list_index], 'priority']

            if priority == 0:
                candidate_list.remove(candidate_index)
                break
            elif priority == 1:
                # lowest candidate wins
                if candidate_index > lowest_candidate:
                    candidate_list.remove(candidate_index)
                    break
            elif priority == 2:
                if candidate_index - table_offset == 10 and hand.suits[Suits.HEART].length == 4:
                    candidate_list.remove(candidate_index)
                    break
                elif candidate_index - table_offset == 11 and hand.suits[Suits.SPADE].length == 4:
                    candidate_list.remove(candidate_index)
                    break
                # lowest candidate wins
                if candidate_index > lowest_candidate:
                    candidate_list.remove(candidate_index)
                    break
            elif priority == 3:
                if candidate_index - table_offset == 5 and hand.suits[Suits.HEART].length == 4:
                    candidate_list.remove(candidate_index)
                    break
                elif candidate_index - table_offset == 6 and hand.suits[Suits.SPADE].length == 4:
                    candidate_list.remove(candidate_index)
                    break
                # lowest candidate wins
                if candidate_index > lowest_candidate:
                    candidate_list.remove(candidate_index)
                    break
            else:   # priority = 4
                # highest candidate wins
                if candidate_index == lowest_candidate:
                    candidate_list.remove(candidate_index)
                    break

            list_index += 1

    if len(candidate_list) > 1:
        print(candidate_list)
        for item in candidate_list:
            print(bid_table.at[item, "bid"])
    elif len(candidate_list) == 0:
        print("oops no candidates")

    index = candidate_list[0]

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
