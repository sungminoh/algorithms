### [2803. Modify Graph Edge Weights](https://leetcode.com/problems/modify-graph-edge-weights/description/?envType=daily-question&envId=2024-08-30)

Hard

You are given an __undirected weighted__ __connected__ graph containing `` n `` nodes labeled from `` 0 `` to `` n - 1 ``, and an integer array `` edges `` where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>, w<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> with weight <code>w<sub>i</sub></code>.

Some edges have a weight of `` -1 `` (<code>w<sub>i</sub> = -1</code>), while others have a __positive__ weight (<code>w<sub>i</sub> > 0</code>).

Your task is to modify __all edges__ with a weight of `` -1 `` by assigning them __positive integer values __in the range <code>[1, 2 * 10<sup>9</sup>]</code> so that the __shortest distance__ between the nodes `` source `` and `` destination `` becomes equal to an integer `` target ``. If there are __multiple__ __modifications__ that make the shortest distance between `` source `` and `` destination `` equal to `` target ``, any of them will be considered correct.

Return _an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from _`` source ``_ to _`` destination ``_ equal to _`` target ``_, or an __empty array__ if it's impossible._

__Note:__ You are not allowed to modify the weights of edges with initial positive weights.

 

<strong class="example">Example 1:</strong>

<strong class="example">

<img alt="" src="https://assets.leetcode.com/uploads/2023/04/18/graph.png" style="width: 300px; height: 300px;"/>

</strong>

```
Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
```

<strong class="example">Example 2:</strong>

<strong class="example">

<img alt="" src="https://assets.leetcode.com/uploads/2023/04/18/graph-2.png" style="width: 300px; height: 300px;"/>

</strong>

```
Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.
```

<strong class="example">Example 3:</strong>

<strong class="example">

<img alt="" src="https://assets.leetcode.com/uploads/2023/04/19/graph-3.png" style="width: 300px; height: 300px;"/>

</strong>

```
Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.
```

 

__Constraints:__

<ul><li><code>1 <= n <= 100</code></li><li><code><font face="monospace">1 <= edges.length <= n * (n - 1) / 2</font></code></li><li><code>edges[i].length == 3</code></li><li><code>0 <= a<sub>i</sub>, b<sub>i </sub>< n</code></li><li><code><font face="monospace">w<sub>i</sub> = -1 </font></code>or <code><font face="monospace">1 <= w<sub>i </sub><= 10<sup><span style="font-size: 10.8333px;">7</span></sup></font></code></li><li><code>a<sub>i </sub>!= b<sub>i</sub></code></li><li><code>0 <= source, destination < n</code></li><li><code>source != destination</code></li><li><code><font face="monospace">1 <= target <= 10<sup>9</sup></font></code></li><li>The graph is connected, and there are no self-loops or repeated edges</li></ul>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 114,109 | 64,687 | 56.7% |