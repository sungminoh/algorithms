### [1263. Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)

Medium

You have `` n `` dice, and each die has `` k `` faces numbered from `` 1 `` to `` k ``.

Given three integers `` n ``, `` k ``, and `` target ``, return _the number of possible ways (out of the _<code>k<sup>n</sup></code>_ total ways) __to roll the dice, so the sum of the face-up numbers equals _`` target ``. Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
```

<strong class="example">Example 2:</strong>

```
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
```

<strong class="example">Example 3:</strong>

```
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 10<sup>9</sup> + 7.
```

 

__Constraints:__

*   `` 1 <= n, k <= 30 ``
*   `` 1 <= target <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 312,677 | 167,423 | 53.5% |