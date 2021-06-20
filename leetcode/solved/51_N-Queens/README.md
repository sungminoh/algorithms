### [51. N-Queens](https://leetcode.com/problems/n-queens/)

Hard

The __n-queens__ puzzle is the problem of placing `` n `` queens on an `` n x n `` chessboard such that no two queens attack each other.

Given an integer `` n ``, return _all distinct solutions to the __n-queens puzzle___. You may return the answer in __any order__.

Each solution contains a distinct board configuration of the n-queens' placement, where `` 'Q' `` and `` '.' `` both indicate a queen and an empty space, respectively.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;"/>

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

__Example 2:__

```
Input: n = 1
Output: [["Q"]]
```

 

__Constraints:__

*   `` 1 <= n <= 9 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 527,013 | 275,216 | 52.2% |