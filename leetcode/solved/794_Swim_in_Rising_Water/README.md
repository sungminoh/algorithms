### [794. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

Hard

You are given an `` n x n `` integer matrix `` grid `` where each value `` grid[i][j] `` represents the elevation at that point `` (i, j) ``.

The rain starts to fall. At time `` t ``, the depth of the water everywhere is `` t ``. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `` t ``. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return _the least time until you can reach the bottom right square _`` (n - 1, n - 1) ``_ if you start at the top left square _`` (0, 0) ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg" style="width: 164px; height: 165px;"/>

```
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg" style="width: 404px; height: 405px;"/>

```
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
```

 

__Constraints:__

*   `` n == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= n <= 50 ``
*   <code>0 <= grid[i][j] < n<sup>2</sup></code>
*   Each value `` grid[i][j] `` is __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 89,484 | 51,599 | 57.7% |