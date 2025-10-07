class Action:
    NEW = 1
    CHANGE = 2
    DELETE = 3


class Side:
    BID = 1
    OFFER = 2


class OrderUpdate:
    """ A message representing an update to an order. """

    def __init__(self, order_id, side, price, size, action):
        """ Construct an individual order update.

        Args:
            order_id (str): The unique ID for this order.
            side (Side): Whether this order is a bid or an offer.
            price (float): The price for this order.
            size (float): The size for this order.
            action (Action): Whether this order is new, changed, or deleted.
        """
        self.order_id = order_id
        self.side = side
        self.price = price
        self.size = size
        self.action = action
