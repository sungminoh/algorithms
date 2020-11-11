### [864. Image Overlap](https://leetcode.com/problems/image-overlap/)

Medium

You are given two images `` img1 `` and `` img2 `` both of size `` n x n ``, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the _overlap_ of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does __not__ include any kind of rotation.)

What is the largest possible overlap?

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg" style="width: 450px; height: 231px;"/>

```
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We slide img1 to right by 1 unit and down by 1 unit.
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg" style="width: 450px; height: 105px;"/>
The number of positions that have a 1 in both images is 3. (Shown in red)
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg" style="width: 450px; height: 231px;"/>
```

__Example 2:__

```
Input: img1 = [[1]], img2 = [[1]]
Output: 1
```

__Example 3:__

```
Input: img1 = [[0]], img2 = [[0]]
Output: 0
```

 

__Constraints:__

*   `` n == img1.length ``
*   `` n == img1[i].length ``
*   `` n == img2.length  ``
*   `` n == img2[i].length ``
*   `` 1 <= n <= 30 ``
*   `` img1[i][j] `` is `` 0 `` or `` 1 ``.
*   `` img2[i][j] `` is `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 66,009 | 41,156 | 62.3% |