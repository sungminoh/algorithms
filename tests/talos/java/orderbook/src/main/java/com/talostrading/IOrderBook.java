package com.talostrading;

import java.util.List;

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
