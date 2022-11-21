### [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

Easy

We are playing the Guess Game. The game is as follows:

I pick a number from `` 1 `` to `` n ``. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `` int guess(int num) ``, which returns three possible results:

*   `` -1 ``: Your guess is higher than the number I picked (i.e. `` num > pick ``).
*   `` 1 ``: Your guess is lower than the number I picked (i.e. `` num < pick ``).
*   `` 0 ``: your guess is equal to the number I picked (i.e. `` num == pick ``).

Return _the number that I picked_.

 

<strong class="example">Example 1:</strong>

```
Input: n = 10, pick = 6
Output: 6
```

<strong class="example">Example 2:</strong>

```
Input: n = 1, pick = 1
Output: 1
```

<strong class="example">Example 3:</strong>

```
Input: n = 2, pick = 1
Output: 1
```

 

__Constraints:__

*   <code>1 <= n <= 2<sup>31</sup> - 1</code>
*   `` 1 <= pick <= n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 870,106 | 447,060 | 51.4% |