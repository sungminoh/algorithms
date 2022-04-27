### [289. Game of Life](https://leetcode.com/problems/game-of-life/)

Medium

According to <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia's article</a>: "The __Game of Life__, also known simply as __Life__, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `` m x n `` grid of cells, where each cell has an initial state: __live__ (represented by a `` 1 ``) or __dead__ (represented by a `` 0 ``). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1.   Any live cell with fewer than two live neighbors dies as if caused by under-population.
2.   Any live cell with two or three live neighbors lives on to the next generation.
3.   Any live cell with more than three live neighbors dies, as if by over-population.
4.   Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

<span>The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the `` m x n `` grid `` board ``, return _the next state_.</span>

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg" style="width: 562px; height: 322px;"/>

```
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg" style="width: 402px; height: 162px;"/>

```
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```

 

__Constraints:__

*   `` m == board.length ``
*   `` n == board[i].length ``
*   `` 1 <= m, n <= 25 ``
*   `` board[i][j] `` is `` 0 `` or `` 1 ``.

 

__Follow up:__

*   Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
*   In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 517,560 | 337,688 | 65.2% |