### [1028. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/description/)

Medium

You are given two lists of closed intervals, `` firstList `` and `` secondList ``, where <code>firstList[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> and <code>secondList[j] = [start<sub>j</sub>, end<sub>j</sub>]</code>. Each list of intervals is pairwise __disjoint__ and in __sorted order__.

Return _the intersection of these two interval lists_.

A __closed interval__ `` [a, b] `` (with `` a <= b ``) denotes the set of real numbers `` x `` with `` a <= x <= b ``.

The __intersection__ of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `` [1, 3] `` and `` [2, 4] `` is `` [2, 3] ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png" style="width: 700px; height: 194px;"/>

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

<strong class="example">Example 2:</strong>

```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

 

__Constraints:__

*   `` 0 <= firstList.length, secondList.length <= 1000 ``
*   `` firstList.length + secondList.length >= 1 ``
*   <code>0 <= start<sub>i</sub> < end<sub>i</sub> <= 10<sup>9</sup></code>
*   <code>end<sub>i</sub> < start<sub>i+1</sub></code>
*   <code>0 <= start<sub>j</sub> < end<sub>j</sub> <= 10<sup>9</sup> </code>
*   <code>end<sub>j</sub> < start<sub>j+1</sub></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 568,899 | 407,375 | 71.6% |