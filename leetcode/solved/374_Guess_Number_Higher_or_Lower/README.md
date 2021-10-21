### [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

Easy

We are playing the Guess Game. The game is as follows:

I pick a number from `` 1 `` to `` n ``. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `` int guess(int num) ``, which returns 3 possible results:

*   `` -1 ``: The number I picked is lower than your guess (i.e. `` pick < num ``).
*   `` 1 ``: The number I picked is higher than your guess (i.e. `` pick > num ``).
*   `` 0 ``: The number I picked is equal to your guess (i.e. `` pick == num ``).

Return _the number that I picked_.

 

__Example 1:__

```Input: n = 10, pick = 6
Output: 6
```

__Example 2:__

```Input: n = 1, pick = 1
Output: 1
```

__Example 3:__

```Input: n = 2, pick = 1
Output: 1
```

__Example 4:__

```Input: n = 2, pick = 2
Output: 2
```

 

__Constraints:__

*   <code>1 <= n <= 2<sup>31</sup> - 1</code>
*   `` 1 <= pick <= n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 535,779 | 253,986 | 47.4% |