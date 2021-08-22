### [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)

Medium

Given an `` m x n `` binary matrix `` mat ``, return _the distance of the nearest _`` 0 ``_ for each cell_.

The distance between two adjacent cells is `` 1 ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg" style="width: 253px; height: 253px;"/>

```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg" style="width: 253px; height: 253px;"/>

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

 

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   <code>1 <= m, n <= 10<sup>4</sup></code>
*   <code>1 <= m * n <= 10<sup>4</sup></code>
*   `` mat[i][j] `` is either `` 0 `` or `` 1 ``.
*   There is at least one `` 0 `` in `` mat ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 375,529 | 160,837 | 42.8% |