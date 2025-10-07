import unittest
import sys
sys.path.append('./')

from orderbook.messages import (
    OrderUpdate,
    Action,
    Side,
)
from orderbook.orderbook import OrderBook


class OrderBookTestSuite(unittest.TestCase):
    """OrderBook test cases."""

    def test_levels(self):
        order_book = OrderBook()
        # empty orderbook
        self.assertEqual(order_book.bids(), [])
        self.assertEqual(order_book.offers(), [])

        # creation
        order_book.on_message(
            OrderUpdate(
                "o1",
                Side.BID,
                3500.00,
                4,
                Action.NEW,
            ))
        self.assertEqual(order_book.bids(), [(3500.00, 4)])
        self.assertEqual(order_book.offers(), [])

        order_book.on_message(
            OrderUpdate(
                "o2",
                Side.OFFER,
                3510.00,
                2,
                Action.NEW,
            ))
        self.assertEqual(order_book.bids(), [(3500.00, 4)])
        self.assertEqual(order_book.offers(), [(3510.00, 2)])

        order_book.on_message(
            OrderUpdate(
                "o1",
                Side.BID,
                3505.00,
                5,
                Action.CHANGE,
            ))
        self.assertEqual(order_book.bids(), [(3505.00, 5)])
        self.assertEqual(order_book.offers(), [(3510.00, 2)])

        order_book.on_message(
            OrderUpdate(
                "o2",
                Side.OFFER,
                0,
                0,
                Action.DELETE,
            ))
        self.assertEqual(order_book.bids(), [(3505.00, 5)])
        self.assertEqual(order_book.offers(), [])


    def test2(self):
        order_book = OrderBook()
        # add bids
        order_book.on_message(OrderUpdate("o1", Side.BID, 3500.00, 4, Action.NEW))
        order_book.on_message(OrderUpdate("o2", Side.BID, 3500.00, 5, Action.NEW))
        order_book.on_message(OrderUpdate("o3", Side.BID, 3100.00, 6, Action.NEW))
        order_book.on_message(OrderUpdate("o4", Side.BID, 3100.00, 7, Action.NEW))
        order_book.on_message(OrderUpdate("o5", Side.BID, 3700.00, 8, Action.NEW))
        # add offers
        order_book.on_message(OrderUpdate("o6", Side.OFFER, 4500.00, 4, Action.NEW))
        order_book.on_message(OrderUpdate("o7", Side.OFFER, 4500.00, 5, Action.NEW))
        order_book.on_message(OrderUpdate("o8", Side.OFFER, 4100.00, 6, Action.NEW))
        order_book.on_message(OrderUpdate("o9", Side.OFFER, 4100.00, 7, Action.NEW))
        order_book.on_message(OrderUpdate("o10", Side.OFFER, 4700.00, 8, Action.NEW))
        self.assertEqual(order_book.bids(), [(3700.00, 8), (3500.00, 9), (3100.00, 13)])
        self.assertEqual(order_book.offers(), [(4100.00, 13), (4500.00, 9), (4700.00, 8)])

        # delete and change
        order_book.on_message(OrderUpdate("o3", Side.BID, 3300.00, 10, Action.CHANGE))
        self.assertEqual(order_book.bids(), [(3700.00, 8), (3500.00, 9), (3300.00, 10), (3100.00, 7)])
        order_book.on_message(OrderUpdate("o7", Side.OFFER, 0, 0, Action.DELETE))
        self.assertEqual(order_book.offers(), [(4100.00, 13), (4500.00, 4), (4700.00, 8)])

    def test_vwap(self):
        order_book = OrderBook()
        # add bids
        order_book.on_message(OrderUpdate("o1", Side.BID, 3500.00, 4, Action.NEW))
        order_book.on_message(OrderUpdate("o2", Side.BID, 3500.00, 5, Action.NEW))
        order_book.on_message(OrderUpdate("o3", Side.BID, 3100.00, 6, Action.NEW))
        order_book.on_message(OrderUpdate("o4", Side.BID, 3100.00, 7, Action.NEW))
        order_book.on_message(OrderUpdate("o5", Side.BID, 3700.00, 8, Action.NEW))
        # add offers
        order_book.on_message(OrderUpdate("o6", Side.OFFER, 4500.00, 4, Action.NEW))
        order_book.on_message(OrderUpdate("o7", Side.OFFER, 4500.00, 5, Action.NEW))
        order_book.on_message(OrderUpdate("o8", Side.OFFER, 4100.00, 6, Action.NEW))
        order_book.on_message(OrderUpdate("o9", Side.OFFER, 4100.00, 7, Action.NEW))
        order_book.on_message(OrderUpdate("o10", Side.OFFER, 4700.00, 8, Action.NEW))
        self.assertEqual(order_book.bids(), [(3700.00, 8), (3500.00, 9), (3100.00, 13)])
        self.assertEqual(order_book.offers(), [(4100.00, 13), (4500.00, 9), (4700.00, 8)])
        self.assertAlmostEqual(order_book.sample_vwap(Side.BID, 6), 3700.00)
        self.assertAlmostEqual(order_book.sample_vwap(Side.BID, 14), 3614.28571429)
        self.assertAlmostEqual(order_book.sample_vwap(Side.OFFER, 31), None)
        self.assertAlmostEqual(order_book.sample_vwap(Side.OFFER, 30), 4380)


if __name__ == "__main__":
    unittest.main()
