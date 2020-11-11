### [488. Zuma Game](https://leetcode.com/problems/zuma-game/)

Hard

Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

 

__Example 1:__

```
Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
```

__Example 2:__

```
Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
```

__Example 3:__

```
Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 
```

__Example 4:__

```
Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
```

 

__Constraints:__

*   You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
*   `` 1 <= board.length <= 16 ``
*   `` 1 <= hand.length <= 5 ``
*   Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 37,067 | 14,689 | 39.6% |