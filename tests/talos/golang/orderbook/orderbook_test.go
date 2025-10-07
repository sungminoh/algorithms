package orderbook

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestOrderBook(t *testing.T) {
	book := NewOrderBook()

	book.OnMessage(OrderUpdate{
		OrderID: "o1",
		Side:    Side.Bid,
		Price:   3500,
		Size:    5,
		Action:  Action.New,
	})
	require.Equal(t, []PriceLevel{
		{Price: 3500, Size: 5},
	}, book.Bids())
	require.Equal(t, []PriceLevel{}, book.Offers())

	book.OnMessage(OrderUpdate{
		OrderID: "o2",
		Side:    Side.Offer,
		Price:   3600,
		Size:    7,
		Action:  Action.New,
	})
	require.Equal(t, []PriceLevel{
		{Price: 3500, Size: 5},
	}, book.Bids())
	require.Equal(t, []PriceLevel{
		{Price: 3600, Size: 7},
	}, book.Offers())

	book.OnMessage(OrderUpdate{
		OrderID: "o2",
		Side:    Side.Offer,
		Price:   3550,
		Size:    9,
		Action:  Action.Change,
	})
	require.Equal(t, []PriceLevel{
		{Price: 3500, Size: 5},
	}, book.Bids())
	require.Equal(t, []PriceLevel{
		{Price: 3550, Size: 9},
	}, book.Offers())

	book.OnMessage(OrderUpdate{
		OrderID: "o2",
		Action:  Action.Delete,
	})
	require.Equal(t, []PriceLevel{
		{Price: 3500, Size: 5},
	}, book.Bids())
	require.Equal(t, []PriceLevel{}, book.Offers())

}
