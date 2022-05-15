### [1753. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

Medium

You are a hiker preparing for an upcoming hike. You are given `` heights ``, a 2D array of size `` rows x columns ``, where `` heights[row][col] `` represents the height of cell `` (row, col) ``. You are situated in the top-left cell, `` (0, 0) ``, and you hope to travel to the bottom-right cell, `` (rows-1, columns-1) `` (i.e., __0-indexed__). You can move __up__, __down__, __left__, or __right__, and you wish to find a route that requires the minimum __effort__.

A route's __effort__ is the __maximum absolute difference____ __in heights between two consecutive cells of the route.

Return _the minimum __effort__ required to travel from the top-left cell to the bottom-right cell._

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/ex1.png" style="width: 300px; height: 300px;"/>

```
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/ex2.png" style="width: 300px; height: 300px;"/>

```
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/04/ex3.png" style="width: 300px; height: 300px;"/>

```
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
```

 

__Constraints:__

*   `` rows == heights.length ``
*   `` columns == heights[i].length ``
*   `` 1 <= rows, columns <= 100 ``
*   <code>1 <= heights[i][j] <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 193,114 | 106,255 | 55.0% |