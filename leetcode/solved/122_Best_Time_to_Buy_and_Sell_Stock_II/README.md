### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

Medium

You are given an integer array `` prices `` where `` prices[i] `` is the price of a given stock on the <code>i<sup>th</sup></code> day.

On each day, you may decide to buy and/or sell the stock. You can only hold __at most one__ share of the stock at any time. However, you can buy it then immediately sell it on the __same day__.

Find and return _the __maximum__ profit you can achieve_.

 

__Example 1:__

```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

__Example 2:__

```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```

__Example 3:__

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```

 

__Constraints:__

*   <code>1 <= prices.length <= 3 * 10<sup>4</sup></code>
*   <code>0 <= prices[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,656,982 | 1,008,376 | 60.9% |