### [1791. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/)

Easy

You are given an `` m x n `` integer grid `` accounts `` where `` accounts[i][j] `` is the amount of money the <code>i​​​​​<sup>​​​​​​th</sup>​​​​</code> customer has in the <code>j​​​​​<sup>​​​​​​th</sup></code>​​​​ bank. Return_ the __wealth__ that the richest customer has._

A customer's __wealth__ is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum __wealth__.

 

__Example 1:__

<strong>Input:</strong> accounts = [[1,2,3],[3,2,1]]
    <strong>Output:</strong> 6
    <strong>Explanation</strong><strong>:</strong>
    1st customer has wealth = 1 + 2 + 3 = 6
    <code>2nd customer has wealth = 3 + 2 + 1 = 6
    </code>Both customers are considered the richest with a wealth of 6 each, so return 6.

__Example 2:__

```
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
```

__Example 3:__

```
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
```

 

__Constraints:__

*   `` m == accounts.length ``
*   `` n == accounts[i].length ``
*   `` 1 <= m, n <= 50 ``
*   `` 1 <= accounts[i][j] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 275,719 | 246,386 | 89.4% |