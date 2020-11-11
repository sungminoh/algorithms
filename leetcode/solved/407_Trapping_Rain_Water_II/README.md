### [407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

Hard

Given an `` m x n `` matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

__Example:__

```
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
```

<img src="https://assets.leetcode.com/uploads/2018/10/13/rainwater_empty.png" style="width: 100%; max-width: 500px;"/>

The above image represents the elevation map `` [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] `` before the rain.

 

<img src="https://assets.leetcode.com/uploads/2018/10/13/rainwater_fill.png" style="width: 100%; max-width: 500px;"/>

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

 

__Constraints:__

*   `` 1 <= m, n <= 110 ``
*   `` 0 <= heightMap[i][j] <= 20000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 105,031 | 45,144 | 43.0% |