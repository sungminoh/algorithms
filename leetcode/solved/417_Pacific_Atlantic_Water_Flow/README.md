### [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

Medium

There is an `` m x n `` rectangular island that borders both the __Pacific Ocean__ and __Atlantic Ocean__. The __Pacific Ocean__ touches the island's left and top edges, and the __Atlantic Ocean__ touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `` m x n `` integer matrix `` heights `` where `` heights[r][c] `` represents the __height above sea level__ of the cell at coordinate `` (r, c) ``.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is __less than or equal to__ the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return _a __2D list__ of grid coordinates _`` result ``_ where _<code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code>_ denotes that rain water can flow from cell _<code>(r<sub>i</sub>, c<sub>i</sub>)</code>_ to __both__ the Pacific and Atlantic oceans_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" style="width: 400px; height: 400px;"/>

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

<strong class="example">Example 2:</strong>

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

 

__Constraints:__

*   `` m == heights.length ``
*   `` n == heights[r].length ``
*   `` 1 <= m, n <= 200 ``
*   <code>0 <= heights[r][c] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 550,019 | 294,748 | 53.6% |