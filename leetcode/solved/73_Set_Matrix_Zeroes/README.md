### [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

Medium

Given an `` m x n `` integer matrix `` matrix ``, if an element is `` 0 ``, set its entire row and column to `` 0 ``'s, and return _the matrix_.

You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" style="width: 450px; height: 169px;"/>

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" style="width: 450px; height: 137px;"/>

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

 

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[0].length ``
*   `` 1 <= m, n <= 200 ``
*   <code>-2<sup>31</sup> <= matrix[i][j] <= 2<sup>31</sup> - 1</code>

 

__Follow up:__

*   A straightforward solution using `` O(mn) `` space is probably a bad idea.
*   A simple improvement uses `` O(m + n) `` space, but still not the best solution.
*   Could you devise a constant space solution?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,126,031 | 523,058 | 46.5% |