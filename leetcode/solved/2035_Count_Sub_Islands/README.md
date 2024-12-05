### [2035. Count Sub Islands](https://leetcode.com/problems/count-sub-islands/description/?envType=daily-question&envId=2024-08-28)

Medium

You are given two `` m x n `` binary matrices `` grid1 `` and `` grid2 `` containing only `` 0 ``'s (representing water) and `` 1 ``'s (representing land). An __island__ is a group of `` 1 ``'s connected __4-directionally__ (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in `` grid2 `` is considered a __sub-island __if there is an island in `` grid1 `` that contains __all__ the cells that make up __this__ island in `` grid2 ``.

Return the ___number__ of islands in _`` grid2 `` _that are considered __sub-islands___.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/test1.png" style="width: 493px; height: 205px;"/>

```
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png" style="width: 491px; height: 201px;"/>

```
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
```

 

__Constraints:__

*   `` m == grid1.length == grid2.length ``
*   `` n == grid1[i].length == grid2[i].length ``
*   `` 1 <= m, n <= 500 ``
*   `` grid1[i][j] `` and `` grid2[i][j] `` are either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 269,779 | 196,463 | 72.8% |