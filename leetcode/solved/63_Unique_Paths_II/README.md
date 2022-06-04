### [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

Medium

You are given an `` m x n `` integer array `` grid ``. There is a robot initially located at the __top-left corner__ (i.e., `` grid[0][0] ``). The robot tries to move to the __bottom-right corner__ (i.e., `` grid[m-1][n-1] ``). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `` 1 `` or `` 0 `` respectively in `` grid ``. A path that the robot takes cannot include __any__ square that is an obstacle.

Return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

The testcases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" style="width: 242px; height: 242px;"/>

```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" style="width: 162px; height: 162px;"/>

```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

 

__Constraints:__

*   `` m == obstacleGrid.length ``
*   `` n == obstacleGrid[i].length ``
*   `` 1 <= m, n <= 100 ``
*   `` obstacleGrid[i][j] `` is `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,430,893 | 550,693 | 38.5% |