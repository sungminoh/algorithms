### [376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

Medium

A __wiggle sequence__ is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

*   For example, `` [1, 7, 4, 9, 2, 5] `` is a __wiggle sequence__ because the differences `` (6, -3, 5, -7, 3) `` alternate between positive and negative.
*   In contrast, `` [1, 4, 7, 2, 5] `` and `` [1, 7, 4, 5, 5] `` are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.

A __subsequence__ is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array `` nums ``, return _the length of the longest __wiggle subsequence__ of _`` nums ``.

 

__Example 1:__

```
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
```

__Example 2:__

```
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
```

__Example 3:__

```
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
```

 

__Constraints:__

*   `` 1 <= nums.length <= 1000 ``
*   `` 0 <= nums[i] <= 1000 ``

 

__Follow up:__ Could you solve this in `` O(n) `` time?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 411,229 | 197,395 | 48.0% |