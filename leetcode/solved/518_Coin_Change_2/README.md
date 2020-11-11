### [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/)

Medium

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

__Example 1:__

```
<b>Input:</b> amount = 5, coins = [1, 2, 5]
<b>Output:</b> 4
<b>Explanation:</b> there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

__Example 2:__

```
<b>Input:</b> amount = 3, coins = [2]
<b>Output:</b> 0
<b>Explanation:</b> the amount of 3 cannot be made up just with coins of 2.
```

__Example 3:__

```
<b>Input:</b> amount = 10, coins = [10] 
<b>Output:</b> 1
```

 

__Note:__

You can assume that

*   0 <= amount <= 5000
*   1 <= coin <= 5000
*   the number of coins is less than 500
*   the answer is guaranteed to fit into signed 32-bit integer

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 186,322 | 88,409 | 47.4% |