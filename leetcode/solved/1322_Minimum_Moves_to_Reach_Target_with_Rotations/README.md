### [1322. Minimum Moves to Reach Target with Rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/description/)

Hard

In an `` n*n `` grid, there is a snake that spans 2 cells and starts moving from the top left corner at `` (0, 0) `` and `` (0, 1) ``. The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at `` (n-1, n-2) `` and `` (n-1, n-1) ``.

In one move the snake can:

<ul><li>Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.</li><li>Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.</li><li>Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from <code>(r, c)</code> and <code>(r, c+1)</code> to <code>(r, c)</code> and <code>(r+1, c)</code>.<br/>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image-2.png" style="width: 300px; height: 134px;"/></li><li>Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from <code>(r, c)</code> and <code>(r+1, c)</code> to <code>(r, c)</code> and <code>(r, c+1)</code>.<br/>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image-1.png" style="width: 300px; height: 121px;"/></li></ul>

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return `` -1 ``.

 

<strong class="example">Example 1:</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/24/image.png" style="width: 400px; height: 439px;"/></strong>

```
Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].
```

<strong class="example">Example 2:</strong>

```
Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9
```

 

__Constraints:__

*   `` 2 <= n <= 100 ``
*   `` 0 <= grid[i][j] <= 1 ``
*   It is guaranteed that the snake starts at empty cells.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 19,101 | 9,448 | 49.5% |