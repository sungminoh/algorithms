### [2038. Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

Medium

You are given an `` m x n `` matrix `` maze `` (__0-indexed__) with empty cells (represented as `` '.' ``) and walls (represented as `` '+' ``). You are also given the `` entrance `` of the maze, where <code>entrance = [entrance<sub>row</sub>, entrance<sub>col</sub>]</code> denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell __up__, __down__, __left__, or __right__. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the __nearest exit__ from the `` entrance ``. An __exit__ is defined as an __empty cell__ that is at the __border__ of the `` maze ``. The `` entrance `` __does not count__ as an exit.

Return _the __number of steps__ in the shortest path from the _`` entrance ``_ to the nearest exit, or _`` -1 ``_ if no such path exists_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg" style="width: 333px; height: 253px;"/>

```
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg" style="width: 253px; height: 253px;"/>

```
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearest3-grid.jpg" style="width: 173px; height: 93px;"/>

```
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
```

 

__Constraints:__

*   `` maze.length == m ``
*   `` maze[i].length == n ``
*   `` 1 <= m, n <= 100 ``
*   `` maze[i][j] `` is either `` '.' `` or `` '+' ``.
*   `` entrance.length == 2 ``
*   <code>0 <= entrance<sub>row</sub> < m</code>
*   <code>0 <= entrance<sub>col</sub> < n</code>
*   `` entrance `` will always be an empty cell.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 72,134 | 31,489 | 43.7% |