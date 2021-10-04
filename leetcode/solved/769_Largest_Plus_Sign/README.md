### [769. Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/)

Medium

You are given an integer `` n ``. You have an `` n x n `` binary grid `` grid `` with all values initially `` 1 ``'s except for some indices given in the array `` mines ``. The <code>i<sup>th</sup></code> element of the array `` mines `` is defined as <code>mines[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> where <code>grid[x<sub>i</sub>][y<sub>i</sub>] == 0</code>.

Return _the order of the largest __axis-aligned__ plus sign of _1_'s contained in _`` grid ``. If there is none, return `` 0 ``.

An __axis-aligned plus sign__ of `` 1 ``'s of order `` k `` has some center `` grid[r][c] == 1 `` along with four arms of length `` k - 1 `` going up, down, left, and right, and made of `` 1 ``'s. Note that there could be `` 0 ``'s or `` 1 ``'s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for `` 1 ``'s.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg" style="width: 404px; height: 405px;"/>

```
Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/13/plus2-grid.jpg" style="width: 84px; height: 85px;"/>

```
Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.
```

 

__Constraints:__

*   `` 1 <= n <= 500 ``
*   `` 1 <= mines.length <= 5000 ``
*   <code>0 <= x<sub>i</sub>, y<sub>i</sub> < n</code>
*   All the pairs <code>(x<sub>i</sub>, y<sub>i</sub>)</code> are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 92,032 | 44,568 | 48.4% |