### [2439. Longest Cycle in a Graph](https://leetcode.com/problems/longest-cycle-in-a-graph/)

Hard

You are given a __directed__ graph of `` n `` nodes numbered from `` 0 `` to `` n - 1 ``, where each node has __at most one__ outgoing edge.

The graph is represented with a given __0-indexed__ array `` edges `` of size `` n ``, indicating that there is a directed edge from node `` i `` to node `` edges[i] ``. If there is no outgoing edge from node `` i ``, then `` edges[i] == -1 ``.

Return _the length of the __longest__ cycle in the graph_. If no cycle exists, return `` -1 ``.

A cycle is a path that starts and ends at the __same__ node.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/06/08/graph4drawio-5.png" style="width: 335px; height: 191px;"/>

```
Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-1.png" style="width: 171px; height: 161px;"/>

```
Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.
```

 

__Constraints:__

*   `` n == edges.length ``
*   <code>2 <= n <= 10<sup>5</sup></code>
*   `` -1 <= edges[i] < n ``
*   `` edges[i] != i ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 122,182 | 61,918 | 50.7% |