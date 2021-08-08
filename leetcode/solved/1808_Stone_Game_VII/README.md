### [1808. Stone Game VII](https://leetcode.com/problems/stone-game-vii/)

Medium

Alice and Bob take turns playing a game, with __Alice starting first__.

There are `` n `` stones arranged in a row. On each player's turn, they can __remove__ either the leftmost stone or the rightmost stone from the row and receive points equal to the __sum__ of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to __minimize the score's difference__. Alice's goal is to __maximize the difference__ in the score.

Given an array of integers `` stones `` where `` stones[i] `` represents the value of the <code>i<sup>th</sup></code> stone __from the left__, return _the __difference__ in Alice and Bob's score if they both play __optimally__._

 

__Example 1:__

```
Input: stones = [5,3,1,4,2]
Output: 6
Explanation: 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
```

__Example 2:__

```
Input: stones = [7,90,5,1,100,10,10,2]
Output: 122
```

 

__Constraints:__

*   `` n == stones.length ``
*   `` 2 <= n <= 1000 ``
*   `` 1 <= stones[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 37,983 | 22,289 | 58.7% |