### [62. Unique Paths](https://leetcode.com/problems/unique-paths/)

Medium

There is a robot on an `` m x n `` grid. The robot is initially located at the __top-left corner__ (i.e., `` grid[0][0] ``). The robot tries to move to the __bottom-right corner__ (i.e., `` grid[m - 1][n - 1] ``). The robot can only move either down or right at any point in time.

Given the two integers `` m `` and `` n ``, return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

The test cases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.

 

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;"/>

```
Input: m = 3, n = 7
Output: 28
```

__Example 2:__

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

 

__Constraints:__

*   `` 1 <= m, n <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,816,087 | 1,120,451 | 61.7% |