# with 15-17 HCP and a balanced hand, which has priority, a 5 card major or no trump?
from bidding.bid_stack import Bid
from cards.suit import Strains, Suits


def or2f_rules(hand, bids, bid_table, candidate_list):
    suit_len_dict = {'spades': len(hand.suits[Suits.SPADE].cards), 'hearts': len(hand.suits[Suits.HEART].cards),
                     'diamonds': len(hand.suits[Suits.DIAMOND].cards), 'clubs': len(hand.suits[Suits.CLUB].cards)}

    partners_strain = bids.get_partners_strain(hand.position)

    if len(candidate_list) > 1:
        priority = bid_table.at[candidate_list[0], 'priority']
        suit = None
        if priority == 0:
            pass
        elif priority == 1:
            pass
        elif priority == 2:
            pass
        elif priority == 3:
            pass
        elif priority == 4:
            pass
        elif priority == 6:
            longest_suit = 0
            sixes = []
            fives = []
            fours = []
            for suit in hand.suits_by_length:
                if suit.length > longest_suit:
                    longest_suit = suit.length
                if suit.length == 6:
                    sixes.append(suit)
                elif suit.length == 5:
                    fives.append(suit)
                elif suit.length == 4:
                    fours.append(suit)

            if longest_suit > 6:
                suit = hand.suits_by_length[0]

            elif longest_suit == 6:
                suit = sixes[0]
                if len(sixes) > 1:
                    if sixes[1].suit > suit.suit:
                        suit = sixes[1]

            elif longest_suit == 5:
                suit = fives[0]
                if len(fives) > 1:
                    if fives[1].suit > suit.suit:
                        suit = fives[1]
            else:
                suit = fours[0]
                if len(fours) > 1:
                    for four in fours:
                        if four.suit < suit.suit:
                            suit = four

            for candidate in candidate_list:
                if bid_table.at[candidate, 'strain'] != suit.get_bid_table_name():
                    candidate_list.remove(candidate)
            # bid longest suit
            # if two 5 card suits bid highest ranking suit
            # if two 4 card suits bit lowest ranking suit
        elif priority == 7:
            pass
        elif priority == 8:
            pass
        elif priority == 9:
            pass
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
