package com.talostrading;

/**
 * PriceLevel represents a price level with a total size.
 */
public class PriceLevel {
    private double price;
    private double size;

    public PriceLevel(final double price, final double size) {
        this.price = price;
        this.size = size;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(final double price) {
        this.price = price;
    }

    public double getSize() {
        return size;
    }

    public void setSize(final double size) {
        this.size = size;
    }
}
