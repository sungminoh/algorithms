### [447. Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/)

Medium

You are given `` n `` `` points `` in the plane that are all __distinct__, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. A __boomerang__ is a tuple of points `` (i, j, k) `` such that the distance between `` i `` and `` j `` equals the distance between `` i `` and `` k `` __(the order of the tuple matters)__.

Return _the number of boomerangs_.

 

__Example 1:__

```
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
```

__Example 2:__

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 2
```

__Example 3:__

```
Input: points = [[1,1]]
Output: 0
```

 

__Constraints:__

*   `` n == points.length ``
*   `` 1 <= n <= 500 ``
*   `` points[i].length == 2 ``
*   <code>-10<sup>4</sup> <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>4</sup></code>
*   All the points are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 136,131 | 71,056 | 52.2% |