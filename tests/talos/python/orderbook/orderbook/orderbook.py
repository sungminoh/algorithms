from typing import List
from typing import Dict
from collections import defaultdict
from orderbook.messages import (
    Action,
    OrderUpdate,
    Side,
)


class OrderBook:
    """ OrderBook maintains a set of orders by price level.
    k updates -> O(k) -> O(k*n) ?? is for updating data structures ordered
    k offer calls
    n the distinct number of prices
    -> O(k*n*logn) -> O(k*n)
    """

    def __init__(self):
        """ Construct an empty OrderBook. """
        self.orders: Dict[str, OrderUpdate] = {}
        # we want these to be sorted map
        self.agg_bids: Dict[float, float] = defaultdict(int)
        self.bid_prices: List[float] = []
        self.agg_offers: Dict[float, float] = defaultdict(int)

    def on_message(self, msg: OrderUpdate):
        """ Apply an order update to the order book.
        TC: O(logn + n) = O(n)

        Args:
          msg (OrderUpdate): The message to process and apply to the order book.
        """
        def validate(msg):
            """O(1)"""
            assert msg.order_id in self.orders
            assert msg.side == self.orders[msg.order_id].side

        def update(side, price, size):
            """O(1)"""
            d = self.agg_bids if side == Side.BID else self.agg_offers
            d[price] += size
            if d[price] == 0:
                d.pop(price)

        if msg.action == Action.NEW:
            assert msg.order_id not in self.orders
            self.orders[msg.order_id] = msg
            update(msg.side, msg.price, msg.size)
        elif msg.action == Action.CHANGE:
            validate(msg)
            prev_order = self.orders[msg.order_id]
            update(prev_order.side, prev_order.price, -prev_order.size)
            self.orders[msg.order_id] = msg
            update(msg.side, msg.price, msg.size)
        elif msg.action == Action.DELETE:
            validate(msg)
            prev_order = self.orders.pop(msg.order_id)
            update(prev_order.side, prev_order.price, -prev_order.size)

    def bids(self):
        """
        Return a list of (price, size) tuples for each bid level in descending order by price.
        TC: O(nlogn) where n is the distinct number of prices
        """
        # return [(p, self.agg_bids.get(p)) for p in reversed(self.bid_prices)]
        return list(sorted(self.agg_bids.items(), reverse=True))

    def offers(self):
        """
        Return a list of (price, size) tuples for each offer level in ascending order by price.
        TC: O(nlogn) where n is the distinct number of prices
        """
        return list(sorted(self.agg_offers.items(), reverse=False))

    def sample_vwap(self, side, size):
        """ Sample the VWAP (e.g. average price) to buy/sell the given size.

        Returns None if insufficient size is available.

        TC: O(n)  from bids or offers calls

        Args:
            side (Side): Whether to sample a bid or an offer.
            size (float): The size to sample a VWAP for.
        """
        price_volumns = []
        if side == Side.BID:
            price_volumns = self.bids()  # O(n)
        elif side == Side.OFFER:
            price_volumns = self.offers()
        total_price = 0
        cnt = 0
        for price, volumn in price_volumns:  # O(n)
            if cnt < size:
                v = min(volumn, size-cnt)
                cnt += v
                total_price += v*price
            else:
                break
        return total_price/cnt if cnt == size else None
