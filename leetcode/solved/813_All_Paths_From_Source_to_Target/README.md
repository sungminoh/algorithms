### [813. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

Medium

Given a directed acyclic graph (__DAG__) of `` n `` nodes labeled from `` 0 `` to `` n - 1 ``, find all possible paths from node `` 0 `` to node `` n - 1 `` and return them in __any order__.

The graph is given as follows: `` graph[i] `` is a list of all nodes you can visit from node `` i `` (i.e., there is a directed edge from node `` i `` to node `` graph[i][j] ``).

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg" style="width: 242px; height: 242px;"/>

```
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg" style="width: 423px; height: 301px;"/>

```
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

__Example 3:__

```
Input: graph = [[1],[]]
Output: [[0,1]]
```

__Example 4:__

```
Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
```

__Example 5:__

```
Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
```

 

__Constraints:__

*   `` n == graph.length ``
*   `` 2 <= n <= 15 ``
*   `` 0 <= graph[i][j] < n ``
*   `` graph[i][j] != i `` (i.e., there will be no self-loops).
*   All the elements of `` graph[i] `` are __unique__.
*   The input graph is __guaranteed__ to be a __DAG__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 270,794 | 217,732 | 80.4% |