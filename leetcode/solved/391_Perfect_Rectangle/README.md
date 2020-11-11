### [391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)

Hard

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as \[1,1,2,2\]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

<div style="float:right"><img src="https://assets.leetcode.com/uploads/2018/10/22/rectangle_perfect.gif" style="width: 249px; height: 250px;"/></div>

__Example 1:__

```
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
```

 

<div style="clear:both"> </div>

<div style="float:right"><img src="https://assets.leetcode.com/uploads/2018/10/22/rectangle_separated.gif" style="width: 249px; height: 250px;"/></div>

__Example 2:__

```
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
```

 

<div style="clear:both"> </div>

<div style="float:right"><img src="https://assets.leetcode.com/uploads/2018/10/22/rectangle_hole.gif" style="width: 249px; height: 250px;"/></div>

__Example 3:__

```
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
```

 

<div style="clear:both"> </div>

<div style="float:right"><img src="https://assets.leetcode.com/uploads/2018/10/22/rectangle_intersect.gif" style="width: 249px; height: 250px;"/></div>

__Example 4:__

```
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
```

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 87,477 | 26,853 | 30.7% |