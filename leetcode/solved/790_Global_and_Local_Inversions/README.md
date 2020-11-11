### [790. Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/)

Medium

We have some permutation `` A `` of `` [0, 1, ..., N - 1] ``, where `` N `` is the length of `` A ``.

The number of (global) inversions is the number of `` i < j `` with `` 0 <= i < j < N `` and `` A[i] > A[j] ``.

The number of local inversions is the number of `` i `` with `` 0 <= i < N `` and `` A[i] > A[i+1] ``.

Return `` true `` if and only if the number of global inversions is equal to the number of local inversions.

__Example 1:__

```
Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
```

__Example 2:__

```
Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
```

__Note:__

*   `` A `` will be a permutation of `` [0, 1, ..., A.length - 1] ``.
*   `` A `` will have length in range `` [1, 5000] ``.
*   The time limit for this problem has been reduced.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 53,802 | 22,731 | 42.2% |