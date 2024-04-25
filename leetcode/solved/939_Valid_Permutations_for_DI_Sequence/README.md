### [939. Valid Permutations for DI Sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence/description/)

Hard

You are given a string `` s `` of length `` n `` where `` s[i] `` is either:

*   `` 'D' `` means decreasing, or
*   `` 'I' `` means increasing.

A permutation `` perm `` of `` n + 1 `` integers of all the integers in the range `` [0, n] `` is called a __valid permutation__ if for all valid `` i ``:

*   If `` s[i] == 'D' ``, then `` perm[i] > perm[i + 1] ``, and
*   If `` s[i] == 'I' ``, then `` perm[i] < perm[i + 1] ``.

Return _the number of __valid permutations__ _`` perm ``. Since the answer may be large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: s = "DID"
Output: 5
Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
```

<strong class="example">Example 2:</strong>

```
Input: s = "D"
Output: 1
```

 

__Constraints:__

*   `` n == s.length ``
*   `` 1 <= n <= 200 ``
*   `` s[i] `` is either `` 'I' `` or `` 'D' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 27,189 | 15,610 | 57.4% |