### [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

Medium

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `` points `` where <code>points[i] = [x<sub>start</sub>, x<sub>end</sub>]</code> denotes a balloon whose __horizontal diameter__ stretches between <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code>. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up __directly vertically__ (in the positive y-direction) from different points along the x-axis. A balloon with <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code> is __burst__ by an arrow shot at `` x `` if <code>x<sub>start</sub> <= x <= x<sub>end</sub></code>. There is __no limit__ to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `` points ``, return _the __minimum__ number of arrows that must be shot to burst all balloons_.

 

<strong class="example">Example 1:</strong>

```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
```

<strong class="example">Example 2:</strong>

```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
```

<strong class="example">Example 3:</strong>

```
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
```

 

__Constraints:__

*   <code>1 <= points.length <= 10<sup>5</sup></code>
*   `` points[i].length == 2 ``
*   <code>-2<sup>31</sup> <= x<sub>start</sub> < x<sub>end</sub> <= 2<sup>31</sup> - 1</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 536,074 | 296,328 | 55.3% |