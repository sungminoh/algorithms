### [1043. Grid Illumination](https://leetcode.com/problems/grid-illumination/description/)

Hard

There is a 2D `` grid `` of size `` n x n `` where each cell of this grid has a lamp that is initially __turned off__.

You are given a 2D array of lamp positions `` lamps ``, where <code>lamps[i] = [row<sub>i</sub>, col<sub>i</sub>]</code> indicates that the lamp at <code>grid[row<sub>i</sub>][col<sub>i</sub>]</code> is __turned on__. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it __illuminates its cell__ and __all other cells__ in the same __row, column, or diagonal__.

You are also given another 2D array `` queries ``, where <code>queries[j] = [row<sub>j</sub>, col<sub>j</sub>]</code>. For the <code>j<sup>th</sup></code> query, determine whether <code>grid[row<sub>j</sub>][col<sub>j</sub>]</code> is illuminated or not. After answering the <code>j<sup>th</sup></code> query, __turn off__ the lamp at <code>grid[row<sub>j</sub>][col<sub>j</sub>]</code> and its __8 adjacent lamps__ if they exist. A lamp is adjacent if its cell shares either a side or corner with <code>grid[row<sub>j</sub>][col<sub>j</sub>]</code>.

Return _an array of integers _`` ans ``_,__ where _`` ans[j] ``_ should be _`` 1 ``_ if the cell in the _<code>j<sup>th</sup></code>_ query was illuminated, or _`` 0 ``_ if the lamp was not._

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg" style="width: 750px; height: 209px;"/>

```
Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0<sup>th</sup> query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step1.jpg" style="width: 500px; height: 218px;"/>
The 1<sup>st</sup> query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step2.jpg" style="width: 500px; height: 219px;"/>
```

<strong class="example">Example 2:</strong>

```
Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
Output: [1,1]
```

<strong class="example">Example 3:</strong>

```
Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
Output: [1,1,0]
```

 

__Constraints:__

*   <code>1 <= n <= 10<sup>9</sup></code>
*   `` 0 <= lamps.length <= 20000 ``
*   `` 0 <= queries.length <= 20000 ``
*   `` lamps[i].length == 2 ``
*   <code>0 <= row<sub>i</sub>, col<sub>i</sub> < n</code>
*   `` queries[j].length == 2 ``
*   <code>0 <= row<sub>j</sub>, col<sub>j</sub> < n</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 55,932 | 20,517 | 36.7% |