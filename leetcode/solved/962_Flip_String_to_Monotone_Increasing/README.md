### [962. Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/)

Medium

A binary string is monotone increasing if it consists of some number of `` 0 ``'s (possibly none), followed by some number of `` 1 ``'s (also possibly none).

You are given a binary string `` s ``. You can flip `` s[i] `` changing it from `` 0 `` to `` 1 `` or from `` 1 `` to `` 0 ``.

Return _the minimum number of flips to make _`` s ``_ monotone increasing_.

 

<strong class="example">Example 1:</strong>

```
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
```

<strong class="example">Example 2:</strong>

```
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
```

<strong class="example">Example 3:</strong>

```
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s[i] `` is either `` '0' `` or `` '1' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 281,874 | 173,311 | 61.5% |