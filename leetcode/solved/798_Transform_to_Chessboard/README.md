### [798. Transform to Chessboard](https://leetcode.com/problems/transform-to-chessboard/)

Hard

You are given an `` n x n `` binary grid `` board ``. In each move, you can swap any two rows with each other, or any two columns with each other.

Return _the minimum number of moves to transform the board into a __chessboard board___. If the task is impossible, return `` -1 ``.

A __chessboard board__ is a board where no `` 0 ``'s and no `` 1 ``'s are 4-directionally adjacent.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/chessboard1-grid.jpg" style="width: 500px; height: 145px;"/>

```
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/chessboard2-grid.jpg" style="width: 164px; height: 165px;"/>

```
Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/chessboard3-grid.jpg" style="width: 164px; height: 165px;"/>

```
Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
```

 

__Constraints:__

*   `` n == board.length ``
*   `` n == board[i].length ``
*   `` 2 <= n <= 30 ``
*   `` board[i][j] `` is either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 27,563 | 14,280 | 51.8% |