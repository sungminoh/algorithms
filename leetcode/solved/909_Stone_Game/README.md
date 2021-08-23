### [909. Stone Game](https://leetcode.com/problems/stone-game/)

Medium

Alice and Bob play a game with piles of stones. There are an __even__ number of piles arranged in a row, and each pile has a __positive__ integer number of stones `` piles[i] ``.

The objective of the game is to end with the most stones. The __total__ number of stones across all the piles is __odd__, so there are no ties.

Alice and Bob take turns, with __Alice starting first__. Each turn, a player takes the entire pile of stones either from the __beginning__ or from the __end__ of the row. This continues until there are no more piles left, at which point the person with the __most stones wins__.

Assuming Alice and Bob play optimally, return `` true ``_ if Alice wins the game, or _`` false ``_ if Bob wins_.

 

__Example 1:__

```
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
```

__Example 2:__

```
Input: piles = [3,7,2,3]
Output: true
```

 

__Constraints:__

*   `` 2 <= piles.length <= 500 ``
*   `` piles.length `` is __even__.
*   `` 1 <= piles[i] <= 500 ``
*   `` sum(piles[i]) `` is __odd__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 191,704 | 131,034 | 68.4% |