### [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Medium

You are given an integer array `` height `` of length `` n ``. There are `` n `` vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are `` (i, 0) `` and `` (i, height[i]) ``.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

__Notice__ that you may not slant the container.

 

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;"/>

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

__Example 2:__

```
Input: height = [1,1]
Output: 1
```

 

__Constraints:__

*   `` n == height.length ``
*   <code>2 <= n <= 10<sup>5</sup></code>
*   <code>0 <= height[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,683,055 | 1,446,737 | 53.9% |