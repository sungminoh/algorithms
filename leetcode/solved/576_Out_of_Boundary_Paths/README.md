### [576. Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/)

Medium

There is an __m__ by __n__ grid with a ball. Given the start coordinate __(i,j)__ of the ball, you can move the ball to __adjacent__ cell or cross the grid boundary in four directions (up, down, left, right). However, you can __at most__ move __N__ times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 10<sup>9</sup> + 7.

 

__Example 1:__

```
<b>Input: </b>m = 2, n = 2, N = 2, i = 0, j = 0
<b>Output:</b> 6
<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/13/out_of_boundary_paths_1.png" style="width: 100%; max-width: 400px"/>
```

__Example 2:__

```
<b>Input: </b>m = 1, n = 3, N = 3, i = 0, j = 1
<b>Output:</b> 12
<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/out_of_boundary_paths_2.png" style="width: 100%; max-width: 400px"/>
```

 

__Note:__

1.   Once you move the ball out of boundary, you cannot move it back.
2.   The length and height of the grid is in range \[1,50\].
3.   N is in range \[0,50\].

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 77,358 | 26,747 | 34.6% |