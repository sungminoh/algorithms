### [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

Medium

Given a `` m x n `` `` grid `` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

__Note:__ You can only move either down or right at any point in time.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;"/>

```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```

<strong class="example">Example 2:</strong>

```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 200 ``
*   `` 0 <= grid[i][j] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,498,108 | 929,222 | 62.0% |