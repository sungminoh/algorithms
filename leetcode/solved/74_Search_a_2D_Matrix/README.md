### [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

Medium

Write an efficient algorithm that searches for a value `` target `` in an `` m x n `` integer matrix `` matrix ``. This matrix has the following properties:

*   Integers in each row are sorted from left to right.
*   The first integer of each row is greater than the last integer of the previous row.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;"/>

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg" style="width: 322px; height: 242px;"/>

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

 

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 <= m, n <= 100 ``
*   <code>-10<sup>4</sup> <= matrix[i][j], target <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,712,273 | 756,324 | 44.2% |