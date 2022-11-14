### [1414. Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

Hard

You are given an `` m x n `` integer matrix `` grid `` where each cell is either `` 0 `` (empty) or `` 1 `` (obstacle). You can move up, down, left, or right from and to an empty cell in __one step__.

Return _the minimum number of __steps__ to walk from the upper left corner _`` (0, 0) ``_ to the lower right corner _`` (m - 1, n - 1) ``_ given that you can eliminate __at most__ _`` k ``_ obstacles_. If it is not possible to find such walk return `` -1 ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/30/short1-grid.jpg" style="width: 244px; height: 405px;"/>

```
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/30/short2-grid.jpg" style="width: 244px; height: 245px;"/>

```
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 40 ``
*   `` 1 <= k <= m * n ``
*   `` grid[i][j] `` is either `` 0 `` __or__ `` 1 ``.
*   `` grid[0][0] == grid[m - 1][n - 1] == 0 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 361,333 | 165,051 | 45.7% |