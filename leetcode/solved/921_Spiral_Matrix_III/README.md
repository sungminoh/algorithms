### [921. Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08)

Medium

You start at the cell `` (rStart, cStart) `` of an `` rows x cols `` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all `` rows * cols `` spaces of the grid.

Return _an array of coordinates representing the positions of the grid in the order you visited them_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png" style="width: 174px; height: 99px;"/>

```
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png" style="width: 202px; height: 142px;"/>

```
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
```

 

__Constraints:__

*   `` 1 <= rows, cols <= 100 ``
*   `` 0 <= rStart < rows ``
*   `` 0 <= cStart < cols ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 188,096 | 159,265 | 84.7% |