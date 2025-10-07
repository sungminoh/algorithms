# Go Order Book Project

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

- `OrderID` (string): The unique ID for this order.
- `Side` (`SideEnum`): Whether this order is a `Bid` / `Offer`.
- `Price` (float64): The price for this order.
- `Size` (float64): The size for this order.
- `Action` (`ActionEnum`): Whether this order is `New`, `Change`, or `Delete`.

The skeleton for the `OrderBook` type is specified:

```go
package orderbook
type OrderBook struct {
}
func NewOrderBook() *OrderBook {
	return &OrderBook{}
}
// Apply an OrderUpdate to this OrderBook
func (b *OrderBook) OnMessage(msg OrderUpdate) {
	return
}
// Sample Bid PriceLevels in Decending Price Order
func (b *OrderBook) Bids() []PriceLevel {
	return nil
}
// Sample Offer PriceLevels in Ascending Price Order
func (b *OrderBook) Offers() []PriceLevel {
	return nil
}
```

## Types

Basic types are provided

### SideEnum

```go
// SideEnum represents a side of the market.
type SideValues struct {
	Bid   SideEnum
	Offer SideEnum
}
```

### ActionEnum

```go
// ActionEnum represents a change to an individual order.
type ActionValues struct {
	New    ActionEnum
	Change ActionEnum
	Delete ActionEnum
}
```

### OrderUpdate

```go
// OrderUpdate represents a change to an individual order.
type OrderUpdate struct {
	OrderID string
	Side    SideEnum
	Price   float64
	Size    float64
	Action  ActionEnum
}
```

### PriceLevel

```go
// PriceLevel represents a price level with a total size.
type PriceLevel struct {
	Price float64
	Size  float64
}
```

## Testing

A basic, but not complete, set of tests is provided in `orderbook_test.go`
