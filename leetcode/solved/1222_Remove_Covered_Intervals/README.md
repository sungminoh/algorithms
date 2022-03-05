### [1222. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)

Medium

Given an array `` intervals `` where <code>intervals[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> represent the interval <code>[l<sub>i</sub>, r<sub>i</sub>)</code>, remove all intervals that are covered by another interval in the list.

The interval `` [a, b) `` is covered by the interval `` [c, d) `` if and only if `` c <= a `` and `` b <= d ``.

Return _the number of remaining intervals_.

 

__Example 1:__

```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```

__Example 2:__

```
Input: intervals = [[1,4],[2,3]]
Output: 1
```

 

__Constraints:__

*   `` 1 <= intervals.length <= 1000 ``
*   `` intervals[i].length == 2 ``
*   <code>0 <= l<sub>i</sub> < r<sub>i</sub> <= 10<sup>5</sup></code>
*   All the given intervals are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 162,836 | 93,531 | 57.4% |