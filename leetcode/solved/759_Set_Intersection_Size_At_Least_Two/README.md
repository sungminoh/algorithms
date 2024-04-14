### [759. Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/description/)

Hard

You are given a 2D integer array `` intervals `` where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represents all the integers from <code>start<sub>i</sub></code> to <code>end<sub>i</sub></code> inclusively.

A __containing set__ is an array `` nums `` where each interval from `` intervals `` has __at least two__ integers in `` nums ``.

*   For example, if `` intervals = [[1,3], [3,7], [8,9]] ``, then `` [1,2,4,7,8,9] `` and `` [2,3,4,8,9] `` are __containing sets__.

Return _the minimum possible size of a containing set_.

 

<strong class="example">Example 1:</strong>

```
Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
```

<strong class="example">Example 2:</strong>

```
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
```

<strong class="example">Example 3:</strong>

```
Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.
```

 

__Constraints:__

*   `` 1 <= intervals.length <= 3000 ``
*   `` intervals[i].length == 2 ``
*   <code>0 <= start<sub>i</sub> < end<sub>i</sub> <= 10<sup>8</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 51,049 | 22,644 | 44.4% |