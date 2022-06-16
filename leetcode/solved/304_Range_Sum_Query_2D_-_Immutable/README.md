### [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

Medium

Given a 2D matrix `` matrix ``, handle multiple queries of the following type:

*   Calculate the __sum__ of the elements of `` matrix `` inside the rectangle defined by its __upper left corner__ `` (row1, col1) `` and __lower right corner__ `` (row2, col2) ``.

Implement the `` NumMatrix `` class:

*   `` NumMatrix(int[][] matrix) `` Initializes the object with the integer matrix `` matrix ``.
*   `` int sumRegion(int row1, int col1, int row2, int col2) `` Returns the __sum__ of the elements of `` matrix `` inside the rectangle defined by its __upper left corner__ `` (row1, col1) `` and __lower right corner__ `` (row2, col2) ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg" style="width: 415px; height: 415px;"/>

```
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
```

 

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 <= m, n <= 200 ``
*   <code>-10<sup>4</sup> <= matrix[i][j] <= 10<sup>4</sup></code>
*   `` 0 <= row1 <= row2 < m ``
*   `` 0 <= col1 <= col2 < n ``
*   At most <code>10<sup>4</sup></code> calls will be made to `` sumRegion ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 551,627 | 281,812 | 51.1% |