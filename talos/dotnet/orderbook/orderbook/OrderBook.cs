using System;
using System.Collections.Generic;

namespace orderbook
{
    /// <summary>
    ///     An OrderBook maintains a set of orders by price level.
    /// </summary>
    public class OrderBook
    {
        /// <summary>
        ///     Apply an order update to the order book.
        /// </summary>
        /// <param name="orderUpdate">The message to process and apply to the order book.</param>
        public void OnMessage(OrderUpdate orderUpdate)
        {
            throw new NotImplementedException();
        }

        /// <summary>
        ///     Returns the current list of bid levels in descending order by price.
        /// </summary>
        /// <returns>A list of levels for each bid level in descending order by price.</returns>
        public List<PriceLevel> Bids()
        {
            throw new NotImplementedException();
        }

        /// <summary>
        ///     Returns the current list of offer levels in ascending order by price.
        /// </summary>
        /// <returns>A list of levels for each offer level in ascending order by price.</returns>
        public List<PriceLevel> Offers()
        {
            throw new NotImplementedException();
        }
    }
}