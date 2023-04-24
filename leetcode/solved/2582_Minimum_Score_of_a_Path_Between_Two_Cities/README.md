### [2582. Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)

Medium

You are given a positive integer `` n `` representing `` n `` cities numbered from `` 1 `` to `` n ``. You are also given a __2D__ array `` roads `` where <code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>, distance<sub>i</sub>]</code> indicates that there is a __bidirectional __road between cities <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> with a distance equal to <code>distance<sub>i</sub></code>. The cities graph is not necessarily connected.

The __score__ of a path between two cities is defined as the __minimum __distance of a road in this path.

Return _the __minimum __possible score of a path between cities _`` 1 ``_ and _`` n ``.

__Note__:

*   A path is a sequence of roads between two cities.
*   It is allowed for a path to contain the same road __multiple__ times, and you can visit cities `` 1 `` and `` n `` multiple times along the path.
*   The test cases are generated such that there is __at least__ one path between `` 1 `` and `` n ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph11.png" style="width: 190px; height: 231px;"/>

```
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph22.png" style="width: 190px; height: 231px;"/>

```
Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
```

 

__Constraints:__

*   <code>2 <= n <= 10<sup>5</sup></code>
*   <code>1 <= roads.length <= 10<sup>5</sup></code>
*   `` roads[i].length == 3 ``
*   <code>1 <= a<sub>i</sub>, b<sub>i</sub> <= n</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   <code>1 <= distance<sub>i</sub> <= 10<sup>4</sup></code>
*   There are no repeated edges.
*   There is at least one path between `` 1 `` and `` n ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 121,157 | 70,249 | 58.0% |