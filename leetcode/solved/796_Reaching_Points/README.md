### [796. Reaching Points](https://leetcode.com/problems/reaching-points/description/)

Hard

Given four integers `` sx ``, `` sy ``, `` tx ``, and `` ty ``, return `` true ``_ if it is possible to convert the point _`` (sx, sy) ``_ to the point _`` (tx, ty) `` _through some operations__, or _`` false ``_ otherwise_.

The allowed operation on some point `` (x, y) `` is to convert it to either `` (x, x + y) `` or `` (x + y, y) ``.

 

<strong class="example">Example 1:</strong>

```
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
```

<strong class="example">Example 2:</strong>

```
Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false
```

<strong class="example">Example 3:</strong>

```
Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true
```

 

__Constraints:__

*   <code>1 <= sx, sy, tx, ty <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 197,602 | 65,485 | 33.1% |