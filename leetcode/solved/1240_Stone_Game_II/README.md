### [1240. Stone Game II](https://leetcode.com/problems/stone-game-ii/?envType=daily-question&envId=2023-05-26)

Medium

Alice and Bob continue their games with piles of stones.  There are a number of piles __arranged in a row__, and each pile has a positive integer number of stones `` piles[i] ``.  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, `` M = 1 ``.

On each player's turn, that player can take __all the stones__ in the __first__ `` X `` remaining piles, where `` 1 <= X <= 2M ``.  Then, we set `` M = max(M, X) ``.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

<strong class="example">Example 1:</strong>

```
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
```

<strong class="example">Example 2:</strong>

```
Input: piles = [1,2,3,4,5,100]
Output: 104
```

 

__Constraints:__

*   `` 1 <= piles.length <= 100 ``
*   <code>1 <= piles[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 128,062 | 87,586 | 68.4% |