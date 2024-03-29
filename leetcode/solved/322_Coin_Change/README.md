### [322. Coin Change](https://leetcode.com/problems/coin-change/)

Medium

You are given an integer array `` coins `` representing coins of different denominations and an integer `` amount `` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `` -1 ``.

You may assume that you have an infinite number of each kind of coin.

 

__Example 1:__

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

__Example 2:__

```
Input: coins = [2], amount = 3
Output: -1
```

__Example 3:__

```
Input: coins = [1], amount = 0
Output: 0
```

 

__Constraints:__

*   `` 1 <= coins.length <= 12 ``
*   <code>1 <= coins[i] <= 2<sup>31</sup> - 1</code>
*   <code>0 <= amount <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,540,240 | 1,033,013 | 40.7% |