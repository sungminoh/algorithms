# Java Order Book Project

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

- `OrderID` (str): The unique ID for this order.
- `Side` (`Side`): Whether this order is a `Bid` / `Offer`.
- `Price` (double): The price for this order.
- `Size` (double): The size for this order.
- `Action` (`Action`): Whether this order is `New`, `Change`, or `Delete`.

The interface for the `OrderBook` class is specified:

```java
/**
 * IOrderBook is an interface that maintains a set of orders by price level.
 */
public interface IOrderBook {

    /**
     * Apply an order update to the order book.
     *
     * @param orderUpdate The message to process and apply to the order book.
     */
    void onMessage(final OrderUpdate orderUpdate);

    /**
     * @return a list of levels for each bid level in descending order by price.
     */
    List<PriceLevel> bids();

    /**
     * @return a list of levels for each offer level in ascending order by price.
     */
    List<PriceLevel> offers();
}
}
```

## Data Structures

Example data structures used here are given here in Java.

### Side

```java
/**
 * Side represents a side of the market.
 */
public enum Side {
    Bid,
    Offer
}
```

### Action

```java
/**
 * Action represents a change to an individual order.
 */
public enum Action {
    New,
    Change,
    Delete
}
```

### OrderUpdate

```java
/**
 * OrderUpdate represents a change to an individual order.
 */
public class OrderUpdate {

    private final String orderID;
    private final Side side;
    private final double price;
    private final double size;
    private final Action action;

    public OrderUpdate(final String orderID,
        final Side side,
        final double price,
        final double size,
        final Action action) {
        this.orderID = orderID;
        this.side = side;
        this.price = price;
        this.size = size;
        this.action = action;
    }

    public String getOrderID() {
        return orderID;
    }

    public Side getSide() {
        return side;
    }

    public double getPrice() {
        return price;
    }

    public double getSize() {
        return size;
    }

    public Action getAction() {
        return action;
    }
}
```
### PriceLevel

```java
/**
 * PriceLevel represents a price level with a total size.
 */
public class PriceLevel {
    private double price;
    private double size;

    public PriceLevel(final double price, final double size) {
        this.price = price;
        this.size = size;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(final double price) {
        this.price = price;
    }

    public double getSize() {
        return size;
    }

    public void setSize(final double size) {
        this.size = size;
    }
}
```

### OrderBook

```java
/**
 * OrderBook maintains a set of orders by price level.
 */
public class OrderBook implements IOrderBook {
    @Override
    public void onMessage(final OrderUpdate orderUpdate) {

    }

    @Override
    public List<PriceLevel> bids() {
        return null;
    }

    @Override
    public List<PriceLevel> offers() {
        return null;
    }
}
```

## Testing

An example test might look like the following:

```java
class OrderBookTest {
    @org.junit.jupiter.api.Test
    void testOneBid() {
        final OrderBook orderBook = new OrderBook();
        final var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
            Action.New);
        orderBook.onMessage(orderUpdate1);
        assertEquals(1, orderBook.bids().size(), "one bid");
        assertEquals(100.0, orderBook.bids().get(0).getPrice(), "bid size");
        assertEquals(10.0, orderBook.bids().get(0).getSize(), "bid size");
    }
}
```
