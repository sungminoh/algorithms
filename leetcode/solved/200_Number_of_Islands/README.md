### [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)

Medium

Given an `` m x n `` 2D binary grid `` grid `` which represents a map of `` '1' ``s (land) and `` '0' ``s (water), return _the number of islands_.

An __island__ is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

<strong class="example">Example 1:</strong>

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

<strong class="example">Example 2:</strong>

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 300 ``
*   `` grid[i][j] `` is `` '0' `` or `` '1' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 4,555,869 | 2,709,970 | 59.5% |