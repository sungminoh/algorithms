### [870. Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid/)

Medium

A `` 3 x 3 `` magic square is a `` 3 x 3 `` grid filled with distinct numbers __from __`` 1 ``__ to __`` 9 `` such that each row, column, and both diagonals all have the same sum.

Given a `` row x col `` `` grid `` of integers, how many `` 3 x 3 `` "magic square" subgrids are there?  (Each subgrid is contiguous).

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg" style="width: 322px; height: 242px;"/>

```
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg" style="width: 242px; height: 242px;"/>
while this one is not:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg" style="width: 242px; height: 242px;"/>
In total, there is only one magic square inside the given grid.
```

__Example 2:__

```
Input: grid = [[8]]
Output: 0
```

__Example 3:__

```
Input: grid = [[4,4],[3,3]]
Output: 0
```

__Example 4:__

```
Input: grid = [[4,7,8],[9,5,1],[2,3,6]]
Output: 0
```

 

__Constraints:__

*   `` row == grid.length ``
*   `` col == grid[i].length ``
*   `` 1 <= row, col <= 10 ``
*   `` 0 <= grid[i][j] <= 15 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 67,852 | 25,330 | 37.3% |