### [911. Profitable Schemes](https://leetcode.com/problems/profitable-schemes/?envType=daily-question&envId=2023-04-21)

Hard

There is a group of `` n `` members, and a list of various crimes they could commit. The <code>i<sup>th</sup></code> crime generates a `` profit[i] `` and requires `` group[i] `` members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a __profitable scheme__ any subset of these crimes that generates at least `` minProfit `` profit, and the total number of members participating in that subset of crimes is at most `` n ``.

Return the number of schemes that can be chosen. Since the answer may be very large, __return it modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
```

<strong class="example">Example 2:</strong>

```
Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
```

 

__Constraints:__

*   `` 1 <= n <= 100 ``
*   `` 0 <= minProfit <= 100 ``
*   `` 1 <= group.length <= 100 ``
*   `` 1 <= group[i] <= 100 ``
*   `` profit.length == group.length ``
*   `` 0 <= profit[i] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 120,345 | 58,856 | 48.9% |