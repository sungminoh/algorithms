### [747. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

Easy

You are given an integer array `` cost `` where `` cost[i] `` is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `` 0 ``, or the step with index `` 1 ``.

Return _the minimum cost to reach the top of the floor_.

 

__Example 1:__

```
Input: cost = [10,<u>15</u>,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

__Example 2:__

```
Input: cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

 

__Constraints:__

*   `` 2 <= cost.length <= 1000 ``
*   `` 0 <= cost[i] <= 999 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 969,431 | 596,007 | 61.5% |