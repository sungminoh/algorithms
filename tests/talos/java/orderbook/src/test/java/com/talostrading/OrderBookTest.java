package com.talostrading;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

import static org.junit.jupiter.api.Assertions.assertEquals;

class OrderBookTest {

    private OrderBook orderBook;

    @BeforeEach
    void setUp() {
        orderBook = new OrderBook();
    }

    @AfterEach
    void tearDown() {
        orderBook = null;
    }

    @org.junit.jupiter.api.Test
    void testOneBid() {
        final var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
            Action.New);
        orderBook.onMessage(orderUpdate1);
        assertEquals(1, orderBook.bids().size(), "one bid");
        assertEquals(100.0, orderBook.bids().get(0).getPrice(), "bid size");
        assertEquals(10.0, orderBook.bids().get(0).getSize(), "bid size");
    }

    @org.junit.jupiter.api.Test
    void testBidUpdate() {
        final var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
            Action.New);
        orderBook.onMessage(orderUpdate1);
        final var orderUpdate2 = new OrderUpdate("1", Side.Bid, 100.00, 7.0,
            Action.Change);
        orderBook.onMessage(orderUpdate2);
        assertEquals(1, orderBook.bids().size(), "one bid");
        assertEquals(100.0, orderBook.bids().get(0).getPrice(), "bid[0] size");
        assertEquals(7.0, orderBook.bids().get(0).getSize(), "bid[0] size");
        final var orderUpdate3 = new OrderUpdate("1", Side.Bid, 100.00, 0.0,
            Action.Delete);
        orderBook.onMessage(orderUpdate3);
        assertEquals(0, orderBook.bids().size(), "no bids");
    }

    @org.junit.jupiter.api.Test
    void testMultipleBids() {
        final var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
            Action.New);
        orderBook.onMessage(orderUpdate1);
        final var orderUpdate2 = new OrderUpdate("2", Side.Bid, 101.00, 7.0,
            Action.New);
        orderBook.onMessage(orderUpdate2);
        final var orderUpdate3 = new OrderUpdate("3", Side.Bid, 100.00, 5.0,
            Action.New);
        orderBook.onMessage(orderUpdate3);
        assertEquals(2, orderBook.bids().size(), "two levels");
        assertEquals(101.0, orderBook.bids().get(0).getPrice(), "bid[0] price");
        assertEquals(7.0, orderBook.bids().get(0).getSize(), "bid[0] size");
        assertEquals(100.0, orderBook.bids().get(1).getPrice(), "bid[1] price");
        assertEquals(15.0, orderBook.bids().get(1).getSize(), "bid[1] size");
    }

    @org.junit.jupiter.api.Test
    void testMultipleOffers() {
        final var orderUpdate1 = new OrderUpdate("1", Side.Offer, 100.00, 10.0,
            Action.New);
        orderBook.onMessage(orderUpdate1);
        final var orderUpdate2 = new OrderUpdate("2", Side.Offer, 101.00, 7.0,
            Action.New);
        orderBook.onMessage(orderUpdate2);
        final var orderUpdate3 = new OrderUpdate("3", Side.Offer, 100.00, 5.0,
            Action.New);
        orderBook.onMessage(orderUpdate3);
        assertEquals(2, orderBook.offers().size(), "two levels");
        assertEquals(100.0, orderBook.offers().get(0).getPrice(), "offer[0] price");
        assertEquals(15.0, orderBook.offers().get(0).getSize(), "offer[0] size");
        assertEquals(101.0, orderBook.offers().get(1).getPrice(), "offer[1] price");
        assertEquals(7.0, orderBook.offers().get(1).getSize(), "offer[1] size");
    }

    @org.junit.jupiter.api.Test
    void testOrderChangeDelete() {
        final var orderUpdate1 = new OrderUpdate("1", Side.Offer, 100.00, 10.0,
            Action.New);
        orderBook.onMessage(orderUpdate1);
        final var orderUpdate2 = new OrderUpdate("1", Side.Offer, 101.00, 7.0,
            Action.Change);
        orderBook.onMessage(orderUpdate2);
        assertEquals(1, orderBook.offers().size(), "one offers");
        assertEquals(101.0, orderBook.offers().get(0).getPrice(), "offer[0] price");
        assertEquals(7.0, orderBook.offers().get(0).getSize(), "offer[0] size");

        final var orderUpdate3 = new OrderUpdate("1", Side.Offer, 0.0, 0.0,
            Action.Delete);
        orderBook.onMessage(orderUpdate3);
        assertEquals(0, orderBook.offers().size(), "no offers");
    }
}
