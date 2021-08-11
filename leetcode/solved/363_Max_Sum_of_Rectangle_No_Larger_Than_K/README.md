### [363. Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

Hard

Given an `` m x n `` matrix `` matrix `` and an integer `` k ``, return _the max sum of a rectangle in the matrix such that its sum is no larger than_ `` k ``.

It is __guaranteed__ that there will be a rectangle with a sum no larger than `` k ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg" style="width: 255px; height: 176px;"/>

```
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
```

__Example 2:__

```
Input: matrix = [[2,2,-1]], k = 3
Output: 3
```

 

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 <= m, n <= 100 ``
*   `` -100 <= matrix[i][j] <= 100 ``
*   <code>-10<sup>5</sup> <= k <= 10<sup>5</sup></code>

 

__Follow up:__ What if the number of rows is much larger than the number of columns?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 181,323 | 72,577 | 40.0% |