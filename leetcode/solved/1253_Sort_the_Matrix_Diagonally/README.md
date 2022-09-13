### [1253. Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/)

Medium

A __matrix diagonal__ is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the __matrix diagonal__ starting from `` mat[2][0] ``, where `` mat `` is a `` 6 x 3 `` matrix, includes cells `` mat[2][0] ``, `` mat[3][1] ``, and `` mat[4][2] ``.

Given an `` m x n `` matrix `` mat `` of integers, sort each __matrix diagonal__ in ascending order and return _the resulting matrix_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/1482_example_1_2.png" style="width: 500px; height: 198px;"/>

```
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
```

__Example 2:__

```
Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
```

 

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   `` 1 <= m, n <= 100 ``
*   `` 1 <= mat[i][j] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 162,739 | 136,176 | 83.7% |