### [733. Flood Fill](https://leetcode.com/problems/flood-fill/)

Easy

An `` image `` is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate `` (sr, sc) `` representing the starting pixel (row and column) of the flood fill, and a pixel value `` newColor ``, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

__Example 1:__  

```
<b>Input:</b> 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
<b>Output:</b> [[2,2,2],[2,2,0],[2,0,1]]
<b>Explanation:</b> 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
```

__Note:__<li>The length of <code>image</code> and <code>image[0]</code> will be in the range <code>[1, 50]</code>.</li><li>The given starting pixel will satisfy <code>0 <= sr < image.length</code> and <code>0 <= sc < image[0].length</code>.</li><li>The value of each color in <code>image[i][j]</code> and <code>newColor</code> will be an integer in <code>[0, 65535]</code>.</li>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 190,166 | 101,815 | 53.5% |