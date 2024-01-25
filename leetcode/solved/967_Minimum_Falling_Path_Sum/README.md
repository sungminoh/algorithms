### [967. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19)

Medium

Given an `` n x n `` array of integers `` matrix ``, return _the __minimum sum__ of any __falling path__ through_ `` matrix ``.

A __falling path__ starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `` (row, col) `` will be `` (row + 1, col - 1) ``, `` (row + 1, col) ``, or `` (row + 1, col + 1) ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg" style="width: 499px; height: 500px;"/>

```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg" style="width: 164px; height: 365px;"/>

```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

 

__Constraints:__

*   `` n == matrix.length == matrix[i].length ``
*   `` 1 <= n <= 100 ``
*   `` -100 <= matrix[i][j] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 614,296 | 398,988 | 65.0% |