### [1380. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/)

Medium

Given a 2D `` grid `` consists of `` 0s `` (land) and `` 1s `` (water).  An _island_ is a maximal 4-directionally connected group of <code><font face="monospace">0</font>s</code> and a _closed island_ is an island __totally__ (all left, top, right, bottom) surrounded by `` 1s. ``

Return the number of _closed islands_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png" style="width: 240px; height: 120px;"/>

```
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png" style="width: 160px; height: 80px;"/>

```
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
```

<strong class="example">Example 3:</strong>

```
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
```

 

__Constraints:__

*   `` 1 <= grid.length, grid[0].length <= 100 ``
*   `` 0 <= grid[i][j] <=1 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 301,944 | 201,468 | 66.7% |