### [1171. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

Medium

Given an `` n x n `` binary matrix `` grid ``, return _the length of the shortest __clear path__ in the matrix_. If there is no clear path, return `` -1 ``.

A __clear path__ in a binary matrix is a path from the __top-left__ cell (i.e., `` (0, 0) ``) to the __bottom-right__ cell (i.e., `` (n - 1, n - 1) ``) such that:

*   All the visited cells of the path are `` 0 ``.
*   All the adjacent cells of the path are __8-directionally__ connected (i.e., they are different and they share an edge or a corner).

The __length of a clear path__ is the number of visited cells of this path.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example1_1.png" style="width: 500px; height: 234px;"/>

```
Input: grid = [[0,1],[1,0]]
Output: 2
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example2_1.png" style="height: 216px; width: 500px;"/>

```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

__Example 3:__

```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

 

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= n <= 100 ``
*   `` grid[i][j] is 0 or 1 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 521,609 | 231,315 | 44.3% |