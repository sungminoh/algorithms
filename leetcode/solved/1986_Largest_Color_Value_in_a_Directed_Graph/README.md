### [1986. Largest Color Value in a Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/?envType=daily-question&envId=2023-04-09)

Hard

There is a __directed graph__ of `` n `` colored nodes and `` m `` edges. The nodes are numbered from `` 0 `` to `` n - 1 ``.

You are given a string `` colors `` where `` colors[i] `` is a lowercase English letter representing the __color__ of the <code>i<sup>th</sup></code> node in this graph (__0-indexed__). You are also given a 2D array `` edges `` where <code>edges[j] = [a<sub>j</sub>, b<sub>j</sub>]</code> indicates that there is a __directed edge__ from node <code>a<sub>j</sub></code> to node <code>b<sub>j</sub></code>.

A valid __path__ in the graph is a sequence of nodes <code>x<sub>1</sub> -> x<sub>2</sub> -> x<sub>3</sub> -> ... -> x<sub>k</sub></code> such that there is a directed edge from <code>x<sub>i</sub></code> to <code>x<sub>i+1</sub></code> for every `` 1 <= i < k ``. The __color value__ of the path is the number of nodes that are colored the __most frequently__ occurring color along that path.

Return _the __largest color value__ of any valid path in the given graph, or _`` -1 ``_ if the graph contains a cycle_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet1.png" style="width: 400px; height: 182px;"/>

<strong>Input:</strong> colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
    <strong>Output:</strong> 3
    <strong>Explanation:</strong> The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet2.png" style="width: 85px; height: 85px;"/>

```
Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
```

 

__Constraints:__

*   `` n == colors.length ``
*   `` m == edges.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>0 <= m <= 10<sup>5</sup></code>
*   `` colors `` consists of lowercase English letters.
*   <code>0 <= a<sub>j</sub>, b<sub>j</sub> < n</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 114,669 | 58,752 | 51.2% |