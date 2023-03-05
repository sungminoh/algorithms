### [1643. Number of Nodes in the Sub-Tree With the Same Label](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)

Medium

You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of `` n `` nodes numbered from `` 0 `` to `` n - 1 `` and exactly `` n - 1 `` `` edges ``. The __root__ of the tree is the node `` 0 ``, and each node of the tree has __a label__ which is a lower-case character given in the string `` labels `` (i.e. The node with the number `` i `` has the label `` labels[i] ``).

The `` edges `` array is given on the form <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>, which means there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.

Return _an array of size `` n ``_ where `` ans[i] `` is the number of nodes in the subtree of the <code>i<sup>th</sup></code> node which have the same label as node `` i ``.

A subtree of a tree `` T `` is the tree consisting of a node in `` T `` and all of its descendant nodes.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/q3e1.jpg" style="width: 400px; height: 291px;"/>

```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/q3e2.jpg" style="width: 300px; height: 253px;"/>

```
Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
Output: [4,2,1,1]
Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/q3e3.jpg" style="width: 300px; height: 253px;"/>

```
Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
Output: [3,2,1,1,1]
```

 

__Constraints:__

*   <code>1 <= n <= 10<sup>5</sup></code>
*   `` edges.length == n - 1 ``
*   `` edges[i].length == 2 ``
*   <code>0 <= a<sub>i</sub>, b<sub>i</sub> < n</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   `` labels.length == n ``
*   `` labels `` is consisting of only of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 140,208 | 77,621 | 55.4% |