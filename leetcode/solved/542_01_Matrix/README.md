### [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)

Medium

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

__Example 1: __

```
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

__Example 2: __

```
<b>Input:</b>
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```

 

__Note:__

1.   The number of elements of the given matrix will not exceed 10,000.
2.   There are at least one 0 in the given matrix.
3.   The cells are adjacent in only four directions: up, down, left and right.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 205,406 | 80,444 | 39.2% |