const assert = require('assert').strict;

const {
    OrderBook,
    OrderUpdate,
    ACTION_NEW,
    ACTION_CHANGE,
    ACTION_DELETE,
    SIDE_BID,
    SIDE_OFFER
} = require("../orderbook/orderbook");

orderBook = new OrderBook();
assert.deepEqual(orderBook.bids(), []);
assert.deepEqual(orderBook.offers(), []);

orderBook.onMessage(
    new OrderUpdate(
        "o1",
        SIDE_BID,
        3500.00,
        4,
        ACTION_NEW,
    ));
assert.deepEqual(orderBook.bids(), [[3500.00, 4]]);
assert.deepEqual(orderBook.offers(), []);

orderBook.onMessage(
    new OrderUpdate(
        "o2",
        SIDE_OFFER,
        3510.00,
        2,
        ACTION_NEW,
    ));
assert.deepEqual(orderBook.bids(), [[3500.00, 4]]);
assert.deepEqual(orderBook.offers(), [[3510.00, 2]]);

orderBook.onMessage(
    new OrderUpdate(
        "o1",
        SIDE_BID,
        3505.00,
        5,
        ACTION_CHANGE,
    ));
assert.deepEqual(orderBook.bids(), [[3505.00, 5]]);
assert.deepEqual(orderBook.offers(), [[3510.00, 2]]);

orderBook.onMessage(
    new OrderUpdate(
        "o2",
        SIDE_OFFER,
        0,
        0,
        ACTION_DELETE,
    ));
assert.deepEqual(orderBook.bids(), [[3505.00, 5]]);
assert.deepEqual(orderBook.offers(), []);
