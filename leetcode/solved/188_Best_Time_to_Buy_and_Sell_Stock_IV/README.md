### [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

Hard

You are given an integer array `` prices `` where `` prices[i] `` is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer `` k ``.

Find the maximum profit you can achieve. You may complete at most `` k `` transactions.

__Note:__ You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

__Example 1:__

```
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

__Example 2:__

```
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```

 

__Constraints:__

*   `` 1 <= k <= 100 ``
*   `` 1 <= prices.length <= 1000 ``
*   `` 0 <= prices[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 849,861 | 318,499 | 37.5% |