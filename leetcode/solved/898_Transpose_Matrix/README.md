### [898. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)

Easy

Given a 2D integer array `` matrix ``, return _the __transpose__ of_ `` matrix ``.

The __transpose__ of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png" style="width: 600px; height: 197px;"/>

 

__Example 1:__

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

__Example 2:__

```
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

 

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 <= m, n <= 1000 ``
*   <code>1 <= m * n <= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= matrix[i][j] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 313,540 | 200,616 | 64.0% |