### [587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/)

Hard

You are given an array `` trees `` where <code>trees[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if __all the trees are enclosed__.

Return _the coordinates of trees that are exactly located on the fence perimeter_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/erect2-plane.jpg" style="width: 509px; height: 500px;"/>

```
Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/erect1-plane.jpg" style="width: 509px; height: 500px;"/>

```
Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]
```

 

__Constraints:__

*   `` 1 <= points.length <= 3000 ``
*   `` points[i].length == 2 ``
*   <code>0 <= x<sub>i</sub>, y<sub>i</sub> <= 100</code>
*   All the given points are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 98,250 | 51,369 | 52.3% |