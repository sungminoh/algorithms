### [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/)

[Description](https://leetcode.com/problems/surrounded-regions/description/)[Hints](https://leetcode.com/problems/surrounded-regions/hints/)[Submissions](https://leetcode.com/problems/surrounded-regions/submissions/)[Discuss](https://leetcode.com/problems/surrounded-regions/discuss/)[Solution](https://leetcode.com/problems/surrounded-regions/solution/)

[Pick One](https://leetcode.com/problems/random-one-question/)

------

Given a 2D board containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example:**

```
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:

```
X X X X
X X X X
X X X X
X O X X
```

**Explanation:**

Surrounded regions shouldn’t be on the border, which means that any `'O'` on the border of the board are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.

------