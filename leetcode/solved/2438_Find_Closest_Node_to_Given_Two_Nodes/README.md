### [2438. Find Closest Node to Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)

Medium

You are given a __directed__ graph of `` n `` nodes numbered from `` 0 `` to `` n - 1 ``, where each node has __at most one__ outgoing edge.

The graph is represented with a given __0-indexed__ array `` edges `` of size `` n ``, indicating that there is a directed edge from node `` i `` to node `` edges[i] ``. If there is no outgoing edge from `` i ``, then `` edges[i] == -1 ``.

You are also given two integers `` node1 `` and `` node2 ``.

Return _the __index__ of the node that can be reached from both _`` node1 ``_ and _`` node2 ``_, such that the __maximum__ between the distance from _`` node1 ``_ to that node, and from _`` node2 ``_ to that node is __minimized___. If there are multiple answers, return the node with the __smallest__ index, and if no possible answer exists, return `` -1 ``.

Note that `` edges `` may contain cycles.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-2.png" style="width: 321px; height: 161px;"/>

```
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-4.png" style="width: 195px; height: 161px;"/>

```
Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
```

 

__Constraints:__

*   `` n == edges.length ``
*   <code>2 <= n <= 10<sup>5</sup></code>
*   `` -1 <= edges[i] < n ``
*   `` edges[i] != i ``
*   `` 0 <= node1, node2 < n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 143,066 | 66,082 | 46.2% |