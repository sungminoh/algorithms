### [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

Medium

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 10<sup>4</sup> balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with x<sub>start</sub> and x<sub>end</sub> bursts by an arrow shot at x if x<sub>start</sub> ≤ x ≤ x<sub>end</sub>. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

__Example:__

```
<b>Input:</b>
[[10,16], [2,8], [1,6], [7,12]]

<b>Output:</b>
2

<b>Explanation:</b>
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
```

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 120,195 | 58,622 | 48.8% |