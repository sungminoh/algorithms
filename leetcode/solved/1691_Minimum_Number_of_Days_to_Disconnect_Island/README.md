### [1691. Minimum Number of Days to Disconnect Island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/?envType=daily-question&envId=2024-08-11)

Hard

You are given an `` m x n `` binary grid `` grid `` where `` 1 `` represents land and `` 0 `` represents water. An __island__ is a maximal __4-directionally__ (horizontal or vertical) connected group of `` 1 ``'s.

The grid is said to be __connected__ if we have __exactly one island__, otherwise is said __disconnected__.

In one day, we are allowed to change __any __single land cell `` (1) `` into a water cell `` (0) ``.

Return _the minimum number of days to disconnect the grid_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/land1.jpg" style="width: 500px; height: 169px;"/>

```
Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/land2.jpg" style="width: 404px; height: 85px;"/>

```
Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 30 ``
*   `` grid[i][j] `` is either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 154,228 | 92,028 | 59.7% |