### [1742. Widest Vertical Area Between Two Points Containing No Points](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/?envType=daily-question&envId=2023-12-21)

Easy

Given `` n `` `` points `` on a 2D plane where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>, Return_ the __widest vertical area__ between two points such that no points are inside the area._

A __vertical area__ is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The __widest vertical area__ is the one with the maximum width.

Note that points __on the edge__ of a vertical area __are not__ considered included in the area.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/19/points3.png" style="width: 276px; height: 371px;"/>

​

```
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
```

<strong class="example">Example 2:</strong>

```
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
```

 

__Constraints:__

*   `` n == points.length ``
*   <code>2 <= n <= 10<sup>5</sup></code>
*   `` points[i].length == 2 ``
*   <code>0 <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 169,099 | 149,128 | 88.2% |