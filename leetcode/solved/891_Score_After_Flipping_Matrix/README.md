### [891. Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/description/?envType=daily-question&envId=2024-05-13)

Medium

You are given an `` m x n `` binary matrix `` grid ``.

A __move__ consists of choosing any row or column and toggling each value in that row or column (i.e., changing all `` 0 ``'s to `` 1 ``'s, and all `` 1 ``'s to `` 0 ``'s).

Every row of the matrix is interpreted as a binary number, and the __score__ of the matrix is the sum of these numbers.

Return _the highest possible __score__ after making any number of __moves__ (including zero moves)_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-toogle1.jpg" style="width: 500px; height: 299px;"/>

```
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
```

<strong class="example">Example 2:</strong>

```
Input: grid = [[0]]
Output: 1
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 20 ``
*   `` grid[i][j] `` is either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 175,923 | 141,490 | 80.4% |