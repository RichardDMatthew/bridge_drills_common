# with 15-17 HCP and a balanced hand, which has priority, a 5 card major or no trump?
from framework.bid_stack import Bid
from cards.suit import Strains, Suits


def or2e_rules(hand, bids, bid_table, candidate_list):
    suit_len_dict = {'spades': len(hand.suits[Suits.SPADE].cards), 'hearts': len(hand.suits[Suits.HEART].cards),
                     'diamonds': len(hand.suits[Suits.DIAMOND].cards), 'clubs': len(hand.suits[Suits.CLUB].cards)}

    partners_strain = bids.get_partners_strain(hand.position)

    if len(candidate_list) > 1:
        priority = bid_table.at[candidate_list[0], 'priority']
        if priority == 3:
            in_suit = False
            partner_already_supported = False
            checked_list = []
            while len(candidate_list) > 1:
                for candidate in candidate_list:
                    # filter out suit support
                    if bid_table.at[candidate, 'strain'] != partners_strain and \
                            bid_table.at[candidate, 'level'] == 2 and candidate not in checked_list:
                        candidate_list.remove(candidate)
                        checked_list.append(candidate)
                        break
                    elif bid_table.at[candidate, 'strain'] == partners_strain and \
                            bid_table.at[candidate, 'level'] == 2 and candidate not in checked_list:
                        in_suit = True
                        partner_already_supported = True
                        checked_list.append(candidate)
                    elif bid_table.at[candidate, 'strain'] == 'spades' and candidate not in checked_list:
                        if partner_already_supported:
                            candidate_list.remove(candidate)
                            break
                        else:
                            in_suit = True
                        checked_list.append(candidate)
                    else:
                        if in_suit and bid_table.at[candidate, 'strain'] == 'no trump' and \
                                candidate not in checked_list:
                            candidate_list.remove(candidate)
        elif priority == 4:
            pass
        elif priority == 6:
            pass
        elif priority == 7:
            pass
        elif priority == 8:
            # if there are more than one candidate one of them was because of supported suit, get rid of no trump bid
            for candidate in candidate_list:
                if bid_table.at[candidate, 'strain'] == 'no trump':
                    candidate_list.remove(candidate)
                    break
        elif priority == 10:
            pass
        elif priority == 11:
            pass
        elif priority == 12:
            pass
        elif priority == 14:
            pass
    # partners_strain = bids.get_partners_strain(hand.position)
    #
    # if partners_strain is not None:
    #     for index in candidate_list:
    #         # there is only spade and heart openings in this rule set
    #         if partners_strain == Suits.SPADE:
    #             if hand.suits[Suits.SPADE].length >= 3:
    #
    #         else:
    #
    #         if bid_table.at[index, "table id"]
    #         print(bid_table.at[index, 'bid'])
    #
    # while len(candidate_list) > 1:
    #     for index in candidate_list:
    #         if bid_table.at[index, "table id"]
    #         print(bid_table.at[index, 'bid'])

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
