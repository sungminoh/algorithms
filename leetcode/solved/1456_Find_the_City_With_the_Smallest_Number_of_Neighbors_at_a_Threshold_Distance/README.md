### [1456. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/?envType=daily-question&envId=2024-07-26)

Medium

There are `` n `` cities numbered from `` 0 `` to `` n-1 ``. Given the array `` edges `` where <code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>, weight<sub>i</sub>]</code> represents a bidirectional and weighted edge between cities <code>from<sub>i</sub></code> and <code>to<sub>i</sub></code>, and given the integer `` distanceThreshold ``.

Return the city with the smallest number of cities that are reachable through some path and whose distance is __at most__ `` distanceThreshold ``, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities ___i___ and ___j___ is equal to the sum of the edges' weights along that path.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_01.png" style="width: 300px; height: 225px;"/>

```
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_02.png" style="width: 300px; height: 225px;"/>

```
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
```

 

__Constraints:__

*   `` 2 <= n <= 100 ``
*   `` 1 <= edges.length <= n * (n - 1) / 2 ``
*   `` edges[i].length == 3 ``
*   <code>0 <= from<sub>i</sub> < to<sub>i</sub> < n</code>
*   <code>1 <= weight<sub>i</sub>, distanceThreshold <= 10^4</code>
*   All pairs <code>(from<sub>i</sub>, to<sub>i</sub>)</code> are distinct.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 299,124 | 203,751 | 68.1% |