### [1257. Rank Transform of a Matrix](https://leetcode.com/problems/rank-transform-of-a-matrix/)

Hard

Given an `` m x n `` `` matrix ``, return _a new matrix _`` answer ``_ where _`` answer[row][col] ``_ is the ____rank__ of _`` matrix[row][col] ``.

The __rank__ is an __integer__ that represents how large an element is compared to other elements. It is calculated using the following rules:

*   The rank is an integer starting from `` 1 ``.
*   If two elements `` p `` and `` q `` are in the __same row or column__, then:	
    
    *   If `` p < q `` then `` rank(p) < rank(q) ``
    *   If `` p == q `` then `` rank(p) == rank(q) ``
    *   If `` p > q `` then `` rank(p) > rank(q) ``
    
    
    
*   The __rank__ should be as __small__ as possible.

It is guaranteed that `` answer `` is unique under the given rules.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/18/rank1.jpg" style="width: 442px; height: 162px;"/>

```
Input: matrix = [[1,2],[3,4]]
Output: [[1,2],[2,3]]
Explanation:
The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/18/rank2.jpg" style="width: 442px; height: 162px;"/>

```
Input: matrix = [[7,7],[7,7]]
Output: [[1,1],[1,1]]
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/18/rank3.jpg" style="width: 601px; height: 322px;"/>

```
Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
```

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/18/rank4.jpg" style="width: 601px; height: 242px;"/>

```
Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
Output: [[5,1,4],[1,2,3],[6,3,1]]
```

 

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 <= m, n <= 500 ``
*   <code>-10<sup>9</sup> <= matrix[row][col] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 37,183 | 15,116 | 40.7% |