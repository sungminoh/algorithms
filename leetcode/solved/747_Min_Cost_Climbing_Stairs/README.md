### [747. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

Easy

You are given an integer array `` cost `` where `` cost[i] `` is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `` 0 ``, or the step with index `` 1 ``.

Return _the minimum cost to reach the top of the floor_.

 

__Example 1:__

```
Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
```

__Example 2:__

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
```

 

__Constraints:__

*   `` 2 <= cost.length <= 1000 ``
*   `` 0 <= cost[i] <= 999 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 503,299 | 269,203 | 53.5% |