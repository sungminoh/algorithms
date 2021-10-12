### [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/)

Hard

The demons had captured the princess and imprisoned her in __the bottom-right corner__ of a `` dungeon ``. The `` dungeon `` consists of `` m x n `` rooms laid out in a 2D grid. Our valiant knight was initially positioned in __the top-left room__ and must fight his way through `` dungeon `` to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to `` 0 `` or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only __rightward__ or __downward__ in each step.

Return _the knight's minimum initial health so that he can rescue the princess_.

__Note__ that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/13/dungeon-grid-1.jpg" style="width: 253px; height: 253px;"/>

```
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
```

__Example 2:__

```
Input: dungeon = [[0]]
Output: 1
```

 

__Constraints:__

*   `` m == dungeon.length ``
*   `` n == dungeon[i].length ``
*   `` 1 <= m, n <= 200 ``
*   `` -1000 <= dungeon[i][j] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 429,039 | 152,176 | 35.5% |