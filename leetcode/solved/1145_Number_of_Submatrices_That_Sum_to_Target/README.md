### [1145. Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)

Hard

Given a `` matrix `` and a `` target ``, return the number of non-empty submatrices that sum to 

<font face="monospace">target</font>

.

A submatrix `` x1, y1, x2, y2 `` is the set of all cells `` matrix[x][y] `` with `` x1 <= x <= x2 `` and `` y1 <= y <= y2 ``.

Two submatrices `` (x1, y1, x2, y2) `` and `` (x1', y1', x2', y2') `` are different if they have some coordinate that is different: for example, if `` x1 != x1' ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/mate1.jpg" style="width: 242px; height: 242px;"/>

```
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
```

__Example 2:__

```
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
```

__Example 3:__

```
Input: matrix = [[904]], target = 0
Output: 0
```

 

__Constraints:__

*   `` 1 <= matrix.length <= 100 ``
*   `` 1 <= matrix[0].length <= 100 ``
*   `` -1000 <= matrix[i] <= 1000 ``
*   `` -10^8 <= target <= 10^8 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 57,391 | 37,269 | 64.9% |