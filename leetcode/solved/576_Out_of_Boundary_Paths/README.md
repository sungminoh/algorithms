### [576. Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/)

Medium

There is an `` m x n `` grid with a ball. The ball is initially at the position `` [startRow, startColumn] ``. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply __at most__ `` maxMove `` moves to the ball.

Given the five integers `` m ``, `` n ``, `` maxMove ``, `` startRow ``, `` startColumn ``, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png" style="width: 500px; height: 296px;"/>

```
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png" style="width: 500px; height: 293px;"/>

```
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
```

 

__Constraints:__

*   `` 1 <= m, n <= 50 ``
*   `` 0 <= maxMove <= 50 ``
*   `` 0 <= startRow < m ``
*   `` 0 <= startColumn < n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 142,230 | 56,295 | 39.6% |