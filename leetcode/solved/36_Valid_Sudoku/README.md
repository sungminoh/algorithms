### [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/?envType=daily-question&envId=2025-08-30)

Medium

Determine if a `` 9 x 9 `` Sudoku board is valid. Only the filled cells need to be validated __according to the following rules__:

1.   Each row must contain the digits `` 1-9 `` without repetition.
2.   Each column must contain the digits `` 1-9 `` without repetition.
3.   Each of the nine `` 3 x 3 `` sub-boxes of the grid must contain the digits `` 1-9 `` without repetition.

__Note:__

*   A Sudoku board (partially filled) could be valid but is not necessarily solvable.
*   Only the filled cells need to be validated according to the mentioned rules.

 

<strong class="example">Example 1:</strong>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px"/>

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

<strong class="example">Example 2:</strong>

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

 

__Constraints:__

*   `` board.length == 9 ``
*   `` board[i].length == 9 ``
*   `` board[i][j] `` is a digit `` 1-9 `` or `` '.' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 3,485,038 | 2,209,539 | 63.4% |