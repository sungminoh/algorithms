### [999. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/description/?envType=daily-question&envId=2024-08-10)

Medium

An `` n x n `` grid is composed of `` 1 x 1 `` squares where each `` 1 x 1 `` square consists of a `` '/' ``, `` '\' ``, or blank space `` ' ' ``. These characters divide the square into contiguous regions.

Given the grid `` grid `` represented as a string array, return _the number of regions_.

Note that backslash characters are escaped, so a `` '\' `` is represented as `` '\\' ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/1.png" style="width: 200px; height: 200px;"/>

```
Input: grid = [" /","/ "]
Output: 2
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/2.png" style="width: 200px; height: 198px;"/>

```
Input: grid = [" /","  "]
Output: 1
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/4.png" style="width: 200px; height: 200px;"/>

```
Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
```

 

__Constraints:__

*   `` n == grid.length == grid[i].length ``
*   `` 1 <= n <= 30 ``
*   `` grid[i][j] `` is either `` '/' ``, `` '\' ``, or `` ' ' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 177,494 | 138,407 | 78.0% |