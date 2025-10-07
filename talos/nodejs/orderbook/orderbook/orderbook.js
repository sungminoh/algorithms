const ACTION_NEW = 1
const ACTION_CHANGE = 2
const ACTION_DELETE = 3

const SIDE_BID = 1
const SIDE_OFFER = 2

/** A message representing an update to an order. **/
class OrderUpdate {
    /** Construct an individual order update.

     @param {string} orderID - The unique ID for this order.
     @param {number} side - Whether this order is a bid or an offer.
     @param {number} price - The price for this order.
     @param {number} size - The size for this order.
     @param {number} action - Whether this order is new, changed, or deleted.
     **/
    constructor(orderID, side, price, size, action) {
        this.orderID = orderID
        this.side = side
        this.price = price
        this.size = size
        this.action = action
    }
}


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

module.exports = {
    ACTION_NEW,
    ACTION_CHANGE,
    ACTION_DELETE,
    SIDE_BID,
    SIDE_OFFER,
    OrderBook,
    OrderUpdate,
}
