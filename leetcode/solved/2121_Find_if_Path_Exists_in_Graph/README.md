### [2121. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

Easy

There is a __bi-directional__ graph with `` n `` vertices, where each vertex is labeled from `` 0 `` to `` n - 1 `` (__inclusive__). The edges in the graph are represented as a 2D integer array `` edges ``, where each <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> denotes a bi-directional edge between vertex <code>u<sub>i</sub></code> and vertex <code>v<sub>i</sub></code>. Every vertex pair is connected by __at most one__ edge, and no vertex has an edge to itself.

You want to determine if there is a __valid path__ that exists from vertex `` source `` to vertex `` destination ``.

Given `` edges `` and the integers `` n ``, `` source ``, and `` destination ``, return `` true ``_ if there is a __valid path__ from _`` source ``_ to _`` destination ``_, or _`` false ``_ otherwise__._

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png" style="width: 141px; height: 121px;"/>

```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png" style="width: 281px; height: 141px;"/>

```
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
```

 

__Constraints:__

*   <code>1 <= n <= 2 * 10<sup>5</sup></code>
*   <code>0 <= edges.length <= 2 * 10<sup>5</sup></code>
*   `` edges[i].length == 2 ``
*   <code>0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1</code>
*   <code>u<sub>i</sub> != v<sub>i</sub></code>
*   `` 0 <= source, destination <= n - 1 ``
*   There are no duplicate edges.
*   There are no self edges.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 417,277 | 218,053 | 52.3% |