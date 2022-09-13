### [1007. Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/)

Medium

Return all __non-negative__ integers of length `` n `` such that the absolute difference between every two consecutive digits is `` k ``.

Note that __every__ number in the answer __must not__ have leading zeros. For example, `` 01 `` has one leading zero and is invalid.

You may return the answer in __any order__.

 

__Example 1:__

```
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
```

__Example 2:__

```
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

 

__Constraints:__

*   `` 2 <= n <= 9 ``
*   `` 0 <= k <= 9 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 192,017 | 109,111 | 56.8% |