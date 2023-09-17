### [1677. Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/?envType=daily-question&envId=2023-05-08)

Easy

Given a square matrix `` mat ``, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png" style="width: 336px; height: 174px;"/>

```
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
```

<strong class="example">Example 2:</strong>

```
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
```

<strong class="example">Example 3:</strong>

```
Input: mat = [[5]]
Output: 5
```

 

__Constraints:__

*   `` n == mat.length == mat[i].length ``
*   `` 1 <= n <= 100 ``
*   `` 1 <= mat[i][j] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 353,401 | 292,470 | 82.8% |