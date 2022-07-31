### [473. Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/)

Medium

You are given an integer array `` matchsticks `` where `` matchsticks[i] `` is the length of the <code>i<sup>th</sup></code> matchstick. You want to use __all the matchsticks__ to make one square. You __should not break__ any stick, but you can link them up, and each matchstick must be used __exactly one time__.

Return `` true `` if you can make this square and `` false `` otherwise.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/matchsticks1-grid.jpg" style="width: 253px; height: 253px;"/>

```
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
```

__Example 2:__

```
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
```

 

__Constraints:__

*   `` 1 <= matchsticks.length <= 15 ``
*   <code>1 <= matchsticks[i] <= 10<sup>8</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 314,656 | 128,034 | 40.7% |