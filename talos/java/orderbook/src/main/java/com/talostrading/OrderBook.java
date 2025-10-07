package com.talostrading;

import java.util.List;

/**
 * OrderBook maintains a set of orders by price level.
 */
public class OrderBook implements IOrderBook {

    @Override
    public void onMessage(final OrderUpdate orderUpdate) {
        throw new java.lang.UnsupportedOperationException("Not implemented yet.");
    }

    @Override
    public List<PriceLevel> bids() {
        throw new java.lang.UnsupportedOperationException("Not implemented yet.");
    }

    @Override
    public List<PriceLevel> offers() {
        throw new java.lang.UnsupportedOperationException("Not implemented yet.");
    }
}
