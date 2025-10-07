package orderbook

type SideEnum int

type SideValues struct {
	Bid   SideEnum
	Offer SideEnum
}

var Side = SideValues{0, 1}

type ActionEnum int

type ActionValues struct {
	New    ActionEnum
	Change ActionEnum
	Delete ActionEnum
}

var Action = ActionValues{0, 1, 2}

type OrderUpdate struct {
	OrderID string
	Side    SideEnum
	Price   float64
	Size    float64
	Action  ActionEnum
}

type PriceLevel struct {
	Price float64
	Size  float64
}
