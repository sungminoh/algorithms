### [880. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii)

Hard

We are given a list of (axis-aligned) `` rectangles ``. Each <code>rectangle[i] = [x<sub>i1</sub>, y<sub>i1</sub>, x<sub>i2</sub>, y<sub>i2</sub>] </code>, where <code>(x<sub>i1</sub>, y<sub>i1</sub>)</code> are the coordinates of the bottom-left corner, and <code>(x<sub>i2</sub>, y<sub>i2</sub>)</code> are the coordinates of the top-right corner of the <code>i<sup>th</sup></code> rectangle.

Find the total area covered by all `` rectangles `` in the plane. Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png" style="width: 600px; height: 450px;"/>

```
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
```

__Example 2:__

```
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10<sup>18</sup> modulo (10<sup>9</sup> + 7), which is (10<sup>9</sup>)<sup>2</sup> = (-7)<sup>2</sup> = 49.
```

 

__Constraints:__

<ul><li><code>1 <= rectangles.length <= 200</code></li><li><code><font face="monospace">rectanges[i].length = 4</font></code></li><li><code>0 <= rectangles[i][j] <= 10<sup>9</sup></code></li><li>The total area covered by all rectangles will never exceed <code>2<sup>63</sup> - 1</code> and thus will fit in a <strong>64-bit</strong> signed integer.</li></ul>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 48,799 | 25,688 | 52.6% |