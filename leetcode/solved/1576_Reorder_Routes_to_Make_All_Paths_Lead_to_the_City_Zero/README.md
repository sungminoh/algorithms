### [1576. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

Medium

There are `` n `` cities numbered from `` 0 `` to `` n - 1 `` and `` n - 1 `` roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by `` connections `` where <code>connections[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents a road from city <code>a<sub>i</sub></code> to city <code>b<sub>i</sub></code>.

This year, there will be a big event in the capital (city `` 0 ``), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city `` 0 ``. Return the __minimum__ number of edges changed.

It's __guaranteed__ that each city can reach city `` 0 `` after reorder.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png" style="width: 311px; height: 189px;"/>

```
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/05/13/sample_2_1819.png" style="width: 509px; height: 79px;"/>

```
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
```

<strong class="example">Example 3:</strong>

```
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
```

 

__Constraints:__

*   <code>2 <= n <= 5 * 10<sup>4</sup></code>
*   `` connections.length == n - 1 ``
*   `` connections[i].length == 2 ``
*   <code>0 <= a<sub>i</sub>, b<sub>i</sub> <= n - 1</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 185,416 | 123,592 | 66.7% |