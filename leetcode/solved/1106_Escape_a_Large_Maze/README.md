### [1106. Escape a Large Maze](https://leetcode.com/problems/escape-a-large-maze/description/)

Hard

There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are `` (x, y) ``.

We start at the <code>source = [s<sub>x</sub>, s<sub>y</sub>]</code> square and want to reach the <code>target = [t<sub>x</sub>, t<sub>y</sub>]</code> square. There is also an array of `` blocked `` squares, where each <code>blocked[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a blocked square with coordinates <code>(x<sub>i</sub>, y<sub>i</sub>)</code>.

Each move, we can walk one square north, east, south, or west if the square is __not__ in the array of `` blocked `` squares. We are also not allowed to walk outside of the grid.

Return `` true ``_ if and only if it is possible to reach the _`` target ``_ square from the _`` source ``_ square through a sequence of valid moves_.

 

<strong class="example">Example 1:</strong>

```
Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.
```

<strong class="example">Example 2:</strong>

```
Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: Because there are no blocked cells, it is possible to reach the target square.
```

 

__Constraints:__

*   `` 0 <= blocked.length <= 200 ``
*   `` blocked[i].length == 2 ``
*   <code>0 <= x<sub>i</sub>, y<sub>i</sub> < 10<sup>6</sup></code>
*   `` source.length == target.length == 2 ``
*   <code>0 <= s<sub>x</sub>, s<sub>y</sub>, t<sub>x</sub>, t<sub>y</sub> < 10<sup>6</sup></code>
*   `` source != target ``
*   It is guaranteed that `` source `` and `` target `` are not blocked.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 61,632 | 21,462 | 34.8% |