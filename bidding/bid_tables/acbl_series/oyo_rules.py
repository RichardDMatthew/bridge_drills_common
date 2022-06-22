
from framework.bid_stack import Bid
from cards.suit import Strains, Suits


def oyo_rules(hand, bids, bid_table, candidate_list):
    suit_len_dict = {'spades': len(hand.suits[Suits.SPADE].cards), 'hearts': len(hand.suits[Suits.HEART].cards),
                     'diamonds': len(hand.suits[Suits.DIAMOND].cards), 'clubs': len(hand.suits[Suits.CLUB].cards)}

    while len(candidate_list) > 1:
        for index in candidate_list:
            print(bid_table.at[index, 'bid'])

    index = candidate_list[0]
    # bridge_log.debug('table id %s bid %s', bid_table.at[index, "table id"], bid_table.at[index, "bid"])
    bid = Bid(hand.position,
              table_id=bid_table.at[index, "table id"],
              bid=bid_table.at[index, "bid"],
              level=bid_table.at[index, "level"],
              strain=bid_table.at[index, "strain"],
              description=bid_table.at[index, "description"],
              reference=bid_table.at[index, "reference"],
              comments=bid_table.at[index, "comments"])
    return bid
