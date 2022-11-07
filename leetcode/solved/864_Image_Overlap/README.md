### [864. Image Overlap](https://leetcode.com/problems/image-overlap/)

Medium

You are given two images, `` img1 `` and `` img2 ``, represented as binary, square matrices of size `` n x n ``. A binary matrix has only `` 0 ``s and `` 1 ``s as values.

We __translate__ one image however we choose by sliding all the `` 1 `` bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the __overlap__ by counting the number of positions that have a `` 1 `` in __both__ images.

Note also that a translation does __not__ include any kind of rotation. Any `` 1 `` bits that are translated outside of the matrix borders are erased.

Return _the largest possible overlap_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg" style="width: 450px; height: 231px;"/>

```
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg" style="width: 450px; height: 105px;"/>
The number of positions that have a 1 in both images is 3 (shown in red).
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg" style="width: 450px; height: 231px;"/>
```

<strong class="example">Example 2:</strong>

```
Input: img1 = [[1]], img2 = [[1]]
Output: 1
```

<strong class="example">Example 3:</strong>

```
Input: img1 = [[0]], img2 = [[0]]
Output: 0
```

 

__Constraints:__

*   `` n == img1.length == img1[i].length ``
*   `` n == img2.length == img2[i].length ``
*   `` 1 <= n <= 30 ``
*   `` img1[i][j] `` is either `` 0 `` or `` 1 ``.
*   `` img2[i][j] `` is either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 133,908 | 85,760 | 64.0% |