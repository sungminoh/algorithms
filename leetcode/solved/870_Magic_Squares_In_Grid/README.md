### [870. Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09)

Medium

A `` 3 x 3 `` __magic square__ is a `` 3 x 3 `` grid filled with distinct numbers __from __1__ to __9 such that each row, column, and both diagonals all have the same sum.

Given a `` row x col `` `` grid `` of integers, how many `` 3 x 3 `` magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, `` grid `` may contain numbers up to 15.

 

<strong class="example">Example 1:</strong>

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

<strong class="example">Example 2:</strong>

```
Input: grid = [[8]]
Output: 0
```

 

__Constraints:__

*   `` row == grid.length ``
*   `` col == grid[i].length ``
*   `` 1 <= row, col <= 10 ``
*   `` 0 <= grid[i][j] <= 15 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 279,277 | 144,333 | 51.7% |