### [1393. Maximum Value of K Coins From Piles](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/?envType=daily-question&envId=2023-04-15)

Hard

There are `` n `` __piles__ of coins on a table. Each pile consists of a __positive number__ of coins of assorted denominations.

In one move, you can choose any coin on __top__ of any pile, remove it, and add it to your wallet.

Given a list `` piles ``, where `` piles[i] `` is a list of integers denoting the composition of the <code>i<sup>th</sup></code> pile from __top to bottom__, and a positive integer `` k ``, return _the __maximum total value__ of coins you can have in your wallet if you choose __exactly___ `` k `` _coins optimally_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/09/e1.png" style="width: 600px; height: 243px;"/>

```
Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.
```

<strong class="example">Example 2:</strong>

```
Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.
```

 

__Constraints:__

*   `` n == piles.length ``
*   `` 1 <= n <= 1000 ``
*   <code>1 <= piles[i][j] <= 10<sup>5</sup></code>
*   `` 1 <= k <= sum(piles[i].length) <= 2000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 97,913 | 59,720 | 61.0% |