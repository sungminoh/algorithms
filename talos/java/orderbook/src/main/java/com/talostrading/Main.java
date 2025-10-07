package com.talostrading;

public class Main {

    public static void main(String[] args) {
        final OrderBook orderBook = new OrderBook();

        final var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
            Action.New);
        orderBook.onMessage(orderUpdate1);
    }
}
