### [1442. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

Medium

There are `` n `` computers numbered from `` 0 `` to `` n - 1 `` connected by ethernet cables `` connections `` forming a network where <code>connections[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents a connection between computers <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `` connections ``. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return _the minimum number of times you need to do this in order to make all the computers connected_. If it is not possible, return `` -1 ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png" style="width: 500px; height: 148px;"/>

```
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png" style="width: 500px; height: 129px;"/>

```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
```

<strong class="example">Example 3:</strong>

```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
```

 

__Constraints:__

*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>1 <= connections.length <= min(n * (n - 1) / 2, 10<sup>5</sup>)</code>
*   `` connections[i].length == 2 ``
*   <code>0 <= a<sub>i</sub>, b<sub>i</sub> < n</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   There are no repeated connections.
*   No two computers are connected by more than one cable.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 275,677 | 171,341 | 62.2% |