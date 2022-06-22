from bidding.bid_stack import Bid, Positions


def open_1c():
    bid = Bid(Positions.NORTH,
              table_id="or1",
              bid="1c",
              level="1",
              strain="clubs",
              next_table='or2e',
              description="",
              reference="",
              comments="")
    return bid


def open_1d():
    bid = Bid(Positions.NORTH,
              table_id="or1",
              bid="1d",
              level="1",
              strain="diamonds",
              next_table='or2e',
              description="",
              reference="",
              comments="")
    return bid


def open_1h():
    bid = Bid(Positions.NORTH,
              table_id="or1",
              bid="1h",
              level="1",
              strain="hearts",
              next_table='or2e',
              description="",
              reference="",
              comments="")
    return bid


def open_1s():
    bid = Bid(Positions.NORTH,
              table_id="or1",
              bid="1s",
              level="1",
              strain="spades",
              next_table='or2e',
              description="",
              reference="",
              comments="")
    return bid


def open_1nt():
    bid = Bid(Positions.NORTH,
              table_id="or1",
              bid="1nt",
              level="1",
              strain="no trump",
              next_table='or2d',
              description="",
              reference="",
              comments="")
    return bid


def respond_1h():
    bid = Bid(Positions.SOUTH,
              table_id="or2e",
              bid="1h",
              level="1",
              strain="hearts",
              next_table='or3f',
              description="",
              reference="",
              comments="")
    return bid


def respond_1nt():
    bid = Bid(Positions.SOUTH,
              table_id="or2e",
              bid="1nt",
              level="1",
              strain="no trump",
              next_table='or3f',
              description="",
              reference="",
              comments="")
    return bid


def respond_2s():
    bid = Bid(Positions.SOUTH,
              table_id="or2e",
              bid="2s",
              level="2",
              strain="spades",
              next_table='or3a',
              description="",
              reference="",
              comments="")
    return bid


def respond_2d():
    bid = Bid(Positions.SOUTH,
              table_id="or2e",
              bid="2d",
              level="2",
              strain="diamonds",
              next_table='or3a',
              description="",
              reference="",
              comments="")
    return bid


def respond_2c():
    bid = Bid(Positions.SOUTH,
              table_id="or2e",
              bid="2c",
              level="2",
              strain="clubs",
              next_table='or3b',
              description="",
              reference="",
              comments="")
    return bid


def respond_3h():
    bid = Bid(Positions.SOUTH,
              table_id="or2e",
              bid="3h",
              level="3",
              strain="hearts",
              next_table='or3c',
              description="",
              reference="",
              comments="")
    return bid


def preload_bids(table_id, bids, hand):
    if table_id == 'or1':
        # no preload
    elif table_id == 'or2a':
        # preload 3 no trump
    elif table_id == 'or2b':
        # preload 2 clubs
    elif table_id == 'or2c':
        # preload 2 no trump
    elif table_id == 'or2d':
        # preload 1 no trump
    elif table_id == 'or2e':
        # preload 1 major
    elif table_id == 'or2f':
        # preload 1 minor
    elif table_id == 'or2g':
        # preload 4 level preempt
    elif table_id == 'or2h':
        # preload 3 level preempt
    elif table_id == 'or2i':
        # preload 2 level preempt
    elif table_id == 'or3a':
        # preload 1 major then 2 of same major
    elif table_id == 'or3b':
        # preload 1 minor then 2 of same minor
    elif table_id == 'or3c':
        # preload 1 suit then 3 of same suit
    elif table_id == 'or3d':
        # preload 1 suit then new suit at 1 level
    elif table_id == 'or3e':
        # preload 1 suit then new suit at 2 level
    elif table_id == 'or3f':
        # preload 1 suit then 1 no trump
    elif table_id == 'or3g':
        # preload 1 suit then 2 no trump
    elif table_id == 'or3h':
        # preload 1 no trump then 4 of major
    elif table_id == 'or3i':
        # preload 1 no trump then 3 of major
    elif table_id == 'or3j':
        # preload 1 no trump then stayman
    elif table_id == 'or3k':
        # preload 1 no trump then jacoby transfer
    elif table_id == 'or3l':
        # preload 1 no trump then jacoby sign off

    return bids, hand

