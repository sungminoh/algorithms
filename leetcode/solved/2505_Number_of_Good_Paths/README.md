### [2505. Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/)

Hard

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of `` n `` nodes numbered from `` 0 `` to `` n - 1 `` and exactly `` n - 1 `` edges.

You are given a __0-indexed__ integer array `` vals `` of length `` n `` where `` vals[i] `` denotes the value of the <code>i<sup>th</sup></code> node. You are also given a 2D integer array `` edges `` where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> denotes that there exists an __undirected__ edge connecting nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>.

A __good path__ is a simple path that satisfies the following conditions:

1.   The starting node and the ending node have the __same__ value.
2.   All nodes between the starting node and the ending node have values __less than or equal to__ the starting node (i.e. the starting node's value should be the maximum value along the path).

Return _the number of distinct good paths_.

Note that a path and its reverse are counted as the __same__ path. For example, `` 0 -> 1 `` is considered to be the same as `` 1 -> 0 ``. A single node is also considered as a valid path.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/08/04/f9caaac15b383af9115c5586779dec5.png" style="width: 400px; height: 333px;"/>

```
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/08/04/149d3065ec165a71a1b9aec890776ff.png" style="width: 273px; height: 350px;"/>

```
Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/08/04/31705e22af3d9c0a557459bc7d1b62d.png" style="width: 100px; height: 88px;"/>

```
Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.
```

 

__Constraints:__

*   `` n == vals.length ``
*   <code>1 <= n <= 3 * 10<sup>4</sup></code>
*   <code>0 <= vals[i] <= 10<sup>5</sup></code>
*   `` edges.length == n - 1 ``
*   `` edges[i].length == 2 ``
*   <code>0 <= a<sub>i</sub>, b<sub>i</sub> < n</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   `` edges `` represents a valid tree.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 82,088 | 47,447 | 57.8% |