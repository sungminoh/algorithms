### [879. Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/)

Medium

You are given an array representing a row of `` seats `` where `` seats[i] = 1 `` represents a person sitting in the <code>i<sup>th</sup></code> seat, and `` seats[i] = 0 `` represents that the <code>i<sup>th</sup></code> seat is empty __(0-indexed)__.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return _that maximum distance to the closest person_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/distance.jpg" style="width: 650px; height: 257px;"/>

```
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
```

__Example 2:__

```
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
```

__Example 3:__

```
Input: seats = [0,1]
Output: 1
```

 

__Constraints:__

*   <code>2 <= seats.length <= 2 * 10<sup>4</sup></code>
*   `` seats[i] `` is `` 0 `` or `` 1 ``.
*   At least one seat is __empty__.
*   At least one seat is __occupied__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 221,233 | 98,412 | 44.5% |