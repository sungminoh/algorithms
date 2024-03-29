### [1961. Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/)

Medium

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `` n `` ice cream bars. You are given an array `` costs `` of length `` n ``, where `` costs[i] `` is the price of the <code>i<sup>th</sup></code> ice cream bar in coins. The boy initially has `` coins `` coins to spend, and he wants to buy as many ice cream bars as possible. 

__Note:__ The boy can buy the ice cream bars in any order.

Return _the __maximum__ number of ice cream bars the boy can buy with _`` coins ``_ coins._

You must solve the problem by counting sort.

 

<strong class="example">Example 1:</strong>

```
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
```

<strong class="example">Example 2:</strong>

```
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.
```

<strong class="example">Example 3:</strong>

```
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
```

 

__Constraints:__

*   `` costs.length == n ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>1 <= costs[i] <= 10<sup>5</sup></code>
*   <code>1 <= coins <= 10<sup>8</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 185,535 | 137,285 | 74.0% |