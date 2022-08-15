### [888. Mirror Reflection](https://leetcode.com/problems/mirror-reflection/)

Medium

There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered `` 0 ``, `` 1 ``, and `` 2 ``.

The square room has walls of length `` p `` and a laser ray from the southwest corner first meets the east wall at a distance `` q `` from the <code>0<sup>th</sup></code> receptor.

Given the two integers `` p `` and `` q ``, return _the number of the receptor that the ray meets first_.

The test cases are guaranteed so that the ray will meet a receptor eventually.

 

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/18/reflection.png" style="width: 218px; height: 217px;"/>

```
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
```

__Example 2:__

```
Input: p = 3, q = 1
Output: 1
```

 

__Constraints:__

*   `` 1 <= q <= p <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 112,571 | 71,039 | 63.1% |