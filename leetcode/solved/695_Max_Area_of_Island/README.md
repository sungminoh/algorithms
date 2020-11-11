### [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

Medium

Given a non-empty 2D array `` grid `` of 0's and 1's, an __island__ is a group of `` 1 ``'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

__Example 1:__

```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,0,<b>1</b>,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,<b>1</b>,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```


Given the above grid, return `` 6 ``. Note the answer is not 11, because the island must be connected 4-directionally.


__Example 2:__

```
[[0,0,0,0,0,0,0,0]]
```


Given the above grid, return `` 0 ``.


__Note:__ The length of each dimension in the given `` grid `` does not exceed 50.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 262,890 | 165,397 | 62.9% |