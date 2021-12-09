### [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

Hard

Given a `` rows x cols `` binary `` matrix `` filled with `` 0 ``'s and `` 1 ``'s, find the largest rectangle containing only `` 1 ``'s and return _its area_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;"/>

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

__Example 2:__

```
Input: matrix = [["0"]]
Output: 0
```

__Example 3:__

```
Input: matrix = [["1"]]
Output: 1
```

 

__Constraints:__

*   `` rows == matrix.length ``
*   `` cols == matrix[i].length ``
*   `` 1 <= row, cols <= 200 ``
*   `` matrix[i][j] `` is `` '0' `` or `` '1' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 652,261 | 272,389 | 41.8% |