
from framework.bid_stack import Bid
from cards.suit import get_suit_value, Suits


def or3d_rules(hand, bids, bid_table, candidate_list):
    suit_len_dict = {'spades': len(hand.suits[Suits.SPADE].cards), 'hearts': len(hand.suits[Suits.HEART].cards),
                     'diamonds': len(hand.suits[Suits.DIAMOND].cards), 'clubs': len(hand.suits[Suits.CLUB].cards)}

    partners_bids = bids.get_partners_bids(hand.position)
    # in this rule set there is only one partner bid
    partner_bid = partners_bids[0]
    partners_strain = partner_bid.strain
    partners_level = int(partner_bid.level)
    my_bids = bids.get_my_bids(hand.position)

    second_suit_list = []
    if len(candidate_list) > 1:
        priority = bid_table.at[candidate_list[0], 'priority']
        suit = None
        if priority == 0:
            pass
        elif priority == 1:
            for index in candidate_list:
                # check for bid as second suit higher ranking than partner's suit
                if my_bids[0].strain != bid_table.at[index, "strain"] and bid_table.at[index, "strain"] != 'no trump':
                    if get_suit_value(bid_table.at[index, "strain"]) > get_suit_value(partners_strain) or \
                            bid_table.at[index, "level"] > partners_level:
                        second_suit_list.append(index)
                # check if original suit
                if my_bids[0].strain == bid_table.at[index, "strain"]:
                    candidate_list = [index]
                    break
            if len(second_suit_list) > 0:
                # find longest second suit high
                # second suit can only be hearts or spades
                if hand.suits[Suits.HEART].length > hand.suits[Suits.SPADE].length:
                    # if there are two second suits spades will be index 0 and hearts will be index 1
                    candidate_list = second_suit_list[1]
                else:
                    candidate_list = second_suit_list[0]
            else:   # candidate list will either have a six suit rebid or 1 nt at this point
                candidate_list = candidate_list[0]
    else:
        candidate_list = candidate_list[0]
    index = candidate_list
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

# def or1_rules(hand, bids, bid_table, candidate_list):
#     suit_len_dict = {'spades': len(hand.suits[Suits.SPADE].cards), 'hearts': len(hand.suits[Suits.HEART].cards),
#                      'diamonds': len(hand.suits[Suits.DIAMOND].cards), 'clubs': len(hand.suits[Suits.CLUB].cards)}
#     # print(suit_len_dict)
#
#     no_trump = False
#     majors = False
#     minors = False
#     minor_length = 0
#     spades = False
#     longest_length = 0
#
#     while len(candidate_list) > 1:
#         for index in candidate_list:
#             print(bid_table.at[index, 'bid'])
#
#             # prefer no trump over suit bid
#             if no_trump:
#                 if bid_table.at[index, 'bid'] == '1s' or bid_table.at[index, 'bid'] == '1h' or \
#                         bid_table.at[index, 'bid'] == '1d' or bid_table.at[index, 'bid'] == '1c':
#                     candidate_list.remove(index)
#                     break
#
#             if bid_table.at[index, 'bid'] == '1nt':
#                 no_trump = True
#                 continue
#
#             # bid longest suit
#             if suit_len_dict[bid_table.at[index, 'strain']] > longest_length:
#                 longest_length = suit_len_dict[bid_table.at[index, 'strain']]
#
#             if suit_len_dict[bid_table.at[index, 'strain']] < longest_length:
#                 candidate_list.remove(index)
#                 break
#
#             if suit_len_dict[bid_table.at[index, 'strain']] == longest_length:
#                 if bid_table.at[index, 'strain'] == 'spades' or bid_table.at[index, 'strain'] == 'hearts':
#                     majors = True
#                     if bid_table.at[index, 'strain'] == 'spades':
#                         spades = True
#                 else:
#                     minors = True
#                     if suit_len_dict[bid_table.at[index, 'strain']] > minor_length:
#                         minor_length = suit_len_dict[bid_table.at[index, 'strain']]
#
#                 if majors:
#                     if bid_table.at[index, 'strain'] == 'diamonds' or bid_table.at[index, 'strain'] == 'clubs':
#                         candidate_list.remove(index)
#                         break
#                     if spades:
#                         if bid_table.at[index, 'strain'] == 'hearts':
#                             candidate_list.remove(index)
#
#                 if minors:
#                     if bid_table.at[index, 'strain'] == 'diamonds':
#                         if suit_len_dict['diamonds'] < suit_len_dict['clubs']:
#                             candidate_list.remove(index)
#                             break
#                         elif suit_len_dict['diamonds'] == suit_len_dict['clubs']:
#                             if suit_len_dict['diamonds'] <= 3:
#                                 candidate_list.remove(index)
#                                 break
#
#                     if bid_table.at[index, 'strain'] == 'clubs':
#                         if suit_len_dict['clubs'] < suit_len_dict['diamonds']:
#                             candidate_list.remove(index)
#                             break
#                         elif suit_len_dict['clubs'] == suit_len_dict['diamonds']:
#                             if suit_len_dict['clubs'] > 3:
#                                 candidate_list.remove(index)
#                                 break
#
#     # if len(candidate_list) > 1:
#     #     for index in candidate_list:
#     #         print('------')
#     #         print(index)
#     index = candidate_list[0]
#     # bridge_log.debug('table id %s bid %s', bid_table.at[index, "table id"], bid_table.at[index, "bid"])
#     bid = Bid(hand.position,
#               table_id=bid_table.at[index, "table id"],
#               bid=bid_table.at[index, "bid"],
#               level=bid_table.at[index, "level"],
#               strain=bid_table.at[index, "strain"],
#               description=bid_table.at[index, "description"],
#               reference=bid_table.at[index, "reference"],
#               comments=bid_table.at[index, "comments"])
#     return bid
