# Nodejs Order Book Project

This project contains a skeleton project for an order book implementation that maintains a set of bid and offer orders.

## Background

An order book contains a set of bid (interests to buy) and offer (interests to sell) orders. It's canonical to organize orders by _side_ (bid or offer), then by price, into levels. Price levels are sorted by how aggressive the order is. Bids with higher prices and offers with lower prices are more aggressive.

## Example

The price of the most aggressive bid should be less than the price of the most aggressive offer, since otherwise the orders would match and produce a trade.

For example, consider 5 orders:

 - bid for 15 @ $99
 - bid for 10 @ $100
 - offer for 3 @ $103
 - offer for 12 @ $103
 - offer for 5 @ $105

They would produce an orderbook with levels as follows:

Bids:

| Price | Size |
| ----- | ---- |
| $100 | 10 |
| $99 | 15 |


Offers:

| Price | Size |
| ----- | ---- |
| $103 | 15 |
| $105 | 5 |

Note that bids are in descending order, offers are in ascending order, and the two offers @ $103 are combined onto the same price level and their sizes are added together.

## Problem

The task is to implement an orderbook that takes a series of messages that indicate new, changed, or deleted orders. An order is identified by a unique `OrderID`. Either the price, size, or both may be changed on an order once it is placed. Side will not change.

A change to an order is represented by a `OrderUpdate` message:

- `orderID` (string): The unique ID for this order.
- `side` (number): Whether this order is a `SIDE_BID` or an `SIDE_OFFER`.
- `price` (number): The price for this order.
- `size` (number): The size for this order.
- `action` (number): Whether this order is `ACTION_NEW`, `ACTION_CHANGED`, or `ACTION_DELETED`.

The interface for the `OrderBook` class is specified:

```javascript
/**
 * OrderBook maintains a set of orders by price level.
 */
class OrderBook {
    /**
     * Construct an empty OrderBook.
     */
    constructor() {
        // TODO
    }

    /**
     * Apply an order update to the order book.
     *
     * @param {OrderUpdate} message - The message to process and apply to the order book.
     */
    onMessage(message) {
        // TODO
    }

    /**
     *  Return a list of [price, size] tuples for each bid level in descending order by price.
     */
    bids() {
        return [];
    }

    /**
     *  Return a list of [price, size] tuples for each offer level in ascending order by price.
     */
    offers() {
        return [];
    }
}
```

## Running

To run the tests (from `nodejs/orderbook` dir):

```sh
    $ nodejs tests/orderbook.test.js
```
