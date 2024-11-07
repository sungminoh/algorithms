### [624. Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16)

Medium

You are given `` m `` `` arrays ``, where each array is sorted in __ascending order__.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `` a `` and `` b `` to be their absolute difference `` |a - b| ``.

Return _the maximum distance_.

 

<strong class="example">Example 1:</strong>

```
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
```

<strong class="example">Example 2:</strong>

```
Input: arrays = [[1],[1]]
Output: 0
```

 

__Constraints:__

*   `` m == arrays.length ``
*   <code>2 <= m <= 10<sup>5</sup></code>
*   `` 1 <= arrays[i].length <= 500 ``
*   <code>-10<sup>4</sup> <= arrays[i][j] <= 10<sup>4</sup></code>
*   `` arrays[i] `` is sorted in __ascending order__.
*   There will be at most <code>10<sup>5</sup></code> integers in all the arrays.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 391,416 | 179,134 | 45.8% |