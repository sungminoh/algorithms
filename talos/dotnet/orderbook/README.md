# .NET Core Order Book Project

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

The `OrderBook` class is specified as follows:

```c#
/// <summary>
///     An OrderBook maintains a set of orders by price level.
/// </summary>
public class OrderBook
{
	/// <summary>
	///     Apply an order update to the order book.
	/// </summary>
	/// <param name="orderUpdate">The message to process and apply to the order book.</param>
	public void OnMessage(OrderUpdate orderUpdate);

	/// <summary>
	///     Returns the current list of bid levels in descending order by price.
	/// </summary>
	/// <returns>A list of levels for each bid level in descending order by price.</returns>
	public List<PriceLevel> Bids();

	/// <summary>
	///     Returns the current list of offer levels in ascending order by price.
	/// </summary>
	/// <returns>A list of levels for each offer level in ascending order by price.</returns>
	public List<PriceLevel> Offers();
}
```

## Data Structures

Example data structures used here are given here in C#.

### Side

```c#
    /// <summary>
    ///     Side represents a side of the market.
    /// </summary>
    public enum Side
    {
        Bid,
        Offer
    }
```

### Action

```c#
/// <summary>
///     Action represents a change to an individual order.
/// </summary>
public enum Action
{
	New,
	Change,
	Delete
}
```

### OrderUpdate

```c#
/// <summary>
///     OrderUpdate represents a change to an individual order.
/// </summary>
public class OrderUpdate
{
	public OrderUpdate(string orderId, Side side, double price, double size, Action action)
	{
		OrderId = orderId;
		Side = side;
		Price = price;
		Size = size;
		Action = action;
	}

	public string OrderId { get; }
	public Side Side { get; }
	public double Price { get; }
	public double Size { get; }
	public Action Action { get; }
}
```

### PriceLevel

```c#
/// <summary>
///     PriceLevel represents a price level with a total size.
/// </summary>
public class PriceLevel
{
	public PriceLevel(double price, double size)
	{
		Price = price;
		Size = size;
	}

	public double Price { get; }
	public double Size { get; }
}
```

## Testing

An example test might look like the following:

```c#
public class OrderBookTest
{
	[Test]
	public void TestOneBid()
	{
		var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
			Action.New);
		_orderBook.OnMessage(orderUpdate1);
		Assert.AreEqual(1, _orderBook.Bids().Count, "one bid");
		Assert.AreEqual(100.0, _orderBook.Bids()[0].Price, "bid size");
		Assert.AreEqual(10.0, _orderBook.Bids()[0].Size, "bid size");
	}
}
```
