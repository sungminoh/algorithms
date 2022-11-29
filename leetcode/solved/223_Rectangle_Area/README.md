### [223. Rectangle Area](https://leetcode.com/problems/rectangle-area/)

Medium

Given the coordinates of two __rectilinear__ rectangles in a 2D plane, return _the total area covered by the two rectangles_.

The first rectangle is defined by its __bottom-left__ corner `` (ax1, ay1) `` and its __top-right__ corner `` (ax2, ay2) ``.

The second rectangle is defined by its __bottom-left__ corner `` (bx1, by1) `` and its __top-right__ corner `` (bx2, by2) ``.

 

<strong class="example">Example 1:</strong>

<img alt="Rectangle Area" src="https://assets.leetcode.com/uploads/2021/05/08/rectangle-plane.png" style="width: 700px; height: 365px;"/>

```
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
```

<strong class="example">Example 2:</strong>

```
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
```

 

__Constraints:__

*   <code>-10<sup>4</sup> <= ax1 <= ax2 <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= ay1 <= ay2 <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= bx1 <= bx2 <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= by1 <= by2 <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 429,001 | 192,519 | 44.9% |