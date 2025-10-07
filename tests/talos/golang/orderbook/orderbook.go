package orderbook

type OrderBook struct {
}

func NewOrderBook() *OrderBook {
	return &OrderBook{}
}

func (b *OrderBook) OnMessage(msg OrderUpdate) {
	return
}

func (b *OrderBook) Bids() []PriceLevel {
	return nil
}

func (b *OrderBook) Offers() []PriceLevel {
	return nil
}
