### [971. Shortest Bridge](https://leetcode.com/problems/shortest-bridge/?envType=daily-question&envId=2023-05-21)

Medium

You are given an `` n x n `` binary matrix `` grid `` where `` 1 `` represents land and `` 0 `` represents water.

An __island__ is a 4-directionally connected group of `` 1 ``'s not connected to any other `` 1 ``'s. There are __exactly two islands__ in `` grid ``.

You may change `` 0 ``'s to `` 1 ``'s to connect the two islands to form __one island__.

Return _the smallest number of _`` 0 ``_'s you must flip to connect the two islands_.

 

<strong class="example">Example 1:</strong>

```
Input: grid = [[0,1],[1,0]]
Output: 1
```

<strong class="example">Example 2:</strong>

```
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

<strong class="example">Example 3:</strong>

```
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```

 

__Constraints:__

*   `` n == grid.length == grid[i].length ``
*   `` 2 <= n <= 100 ``
*   `` grid[i][j] `` is either `` 0 `` or `` 1 ``.
*   There are exactly two islands in `` grid ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 317,579 | 183,418 | 57.8% |