package com.talostrading;

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
