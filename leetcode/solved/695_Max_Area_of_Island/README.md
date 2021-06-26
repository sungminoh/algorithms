### [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

Medium

You are given an `` m x n `` binary matrix `` grid ``. An island is a group of `` 1 ``'s (representing land) connected __4-directionally__ (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The __area__ of an island is the number of cells with a value `` 1 `` in the island.

Return _the maximum __area__ of an island in _`` grid ``. If there is no island, return `` 0 ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;"/>

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

__Example 2:__

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 50 ``
*   `` grid[i][j] `` is either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 428,950 | 285,908 | 66.7% |