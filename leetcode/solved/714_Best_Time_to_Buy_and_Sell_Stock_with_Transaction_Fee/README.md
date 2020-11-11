### [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

Medium

Your are given an array of integers `` prices ``, for which the `` i ``-th element is the price of a given stock on day `` i ``; and a non-negative integer `` fee `` representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

__Example 1:__  

```
<b>Input:</b> prices = [1, 3, 2, 8, 4, 9], fee = 2
<b>Output:</b> 8
<b>Explanation:</b> The maximum profit can be achieved by:
<li>Buying at prices[0] = 1</li><li>Selling at prices[3] = 8</li><li>Buying at prices[4] = 4</li><li>Selling at prices[5] = 9</li>The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```

__Note:__<li><code>0 < prices.length <= 50000</code>.</li><li><code>0 < prices[i] < 50000</code>.</li><li><code>0 <= fee < 50000</code>.</li>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 133,351 | 73,217 | 54.9% |