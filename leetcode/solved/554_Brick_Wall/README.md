### [554. Brick Wall](https://leetcode.com/problems/brick-wall/)

Medium

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the __top__ to the __bottom__ and cross the __least__ bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

__You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks. __

 

__Example:__

```
<b>Input:</b> [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

<b>Output:</b> 2

<b>Explanation:</b> 
<img src="https://assets.leetcode.com/uploads/2018/10/12/brick_wall.png" style="width: 100%; max-width: 350px"/>
```

 

__Note:__

1.   The width sum of bricks in different rows are the same and won't exceed INT\_MAX.
2.   The number of bricks in each row is in range \[1,10,000\]. The height of wall is in range \[1,10,000\]. Total number of bricks of the wall won't exceed 20,000.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 108,270 | 53,671 | 49.6% |