package com.talostrading;

public class Factorial {

    /**
     * Compute n factorial
     * @param n offset in the sequence, should be greater than or equal to zero
     * @return factorial of n
     */
    public static int factorial(final int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
