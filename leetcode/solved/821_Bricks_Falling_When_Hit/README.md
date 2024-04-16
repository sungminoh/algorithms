### [821. Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/description/)

Hard

You are given an `` m x n `` binary `` grid ``, where each `` 1 `` represents a brick and `` 0 `` represents an empty space. A brick is __stable__ if:

*   It is directly connected to the top of the grid, or
*   At least one other brick in its four adjacent cells is __stable__.

You are also given an array `` hits ``, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location <code>hits[i] = (row<sub>i</sub>, col<sub>i</sub>)</code>. The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will __fall__. Once a brick falls, it is __immediately__ erased from the `` grid `` (i.e., it does not land on other stable bricks).

Return _an array _`` result ``_, where each _`` result[i] ``_ is the number of bricks that will __fall__ after the _<code>i<sup>th</sup></code>_ erasure is applied._

__Note__ that an erasure may refer to a location with no brick, and if it does, no bricks drop.

 

<strong class="example">Example 1:</strong>

```
Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [<u>1</u>,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,<u>1</u>,<u>1</u>,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].
```

<strong class="example">Example 2:</strong>

```
Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,<u>1</u>,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [<u>1</u>,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].
```

 

__Constraints:__

*   `` m == grid.length ``
*   `` n == grid[i].length ``
*   `` 1 <= m, n <= 200 ``
*   `` grid[i][j] `` is `` 0 `` or `` 1 ``.
*   <code>1 <= hits.length <= 4 * 10<sup>4</sup></code>
*   `` hits[i].length == 2 ``
*   <code>0 <= x<sub>i </sub><= m - 1</code>
*   <code>0 <= y<sub>i</sub> <= n - 1</code>
*   All <code>(x<sub>i</sub>, y<sub>i</sub>)</code> are unique.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 86,428 | 29,978 | 34.7% |