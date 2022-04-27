### [1386. Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/)

Easy

Given a 2D `` grid `` of size `` m x n `` and an integer `` k ``. You need to shift the `` grid `` `` k `` times.

In one shift operation:

*   Element at `` grid[i][j] `` moves to `` grid[i][j + 1] ``.
*   Element at `` grid[i][n - 1] `` moves to `` grid[i + 1][0] ``.
*   Element at `` grid[m - 1][n - 1] `` moves to `` grid[0][0] ``.

Return the _2D grid_ after applying shift operation `` k `` times.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/05/e1.png" style="width: 400px; height: 178px;"/>

<strong>Input:</strong> grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    <strong>Output:</strong> [[9,1,2],[3,4,5],[6,7,8]]

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/05/e2.png" style="width: 400px; height: 166px;"/>

<strong>Input:</strong> grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    <strong>Output:</strong> [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

__Example 3:__

<strong>Input:</strong> grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    <strong>Output:</strong> [[1,2,3],[4,5,6],[7,8,9]]

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m <= 50 ``
*   `` 1 <= n <= 50 ``
*   `` -1000 <= grid[i][j] <= 1000 ``
*   `` 0 <= k <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 122,304 | 83,269 | 68.1% |