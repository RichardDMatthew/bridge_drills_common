from framework.bid_stack import Bid, Positions


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

