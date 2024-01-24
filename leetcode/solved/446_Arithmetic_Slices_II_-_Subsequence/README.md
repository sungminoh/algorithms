### [446. Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/?envType=daily-question&envId=2024-01-07)

Hard

Given an integer array `` nums ``, return _the number of all the __arithmetic subsequences__ of_ `` nums ``.

A sequence of numbers is called arithmetic if it consists of __at least three elements__ and if the difference between any two consecutive elements is the same.

*   For example, `` [1, 3, 5, 7, 9] ``, `` [7, 7, 7, 7] ``, and `` [3, -1, -5, -9] `` are arithmetic sequences.
*   For example, `` [1, 1, 2, 5, 7] `` is not an arithmetic sequence.

A __subsequence__ of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

*   For example, `` [2,5,10] `` is a subsequence of <code>[1,2,1,<strong><u>2</u></strong>,4,1,<u><strong>5</strong></u>,<u><strong>10</strong></u>]</code>.

The test cases are generated so that the answer fits in __32-bit__ integer.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
```

<strong class="example">Example 2:</strong>

```
Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
```

 

__Constraints:__

*   `` 1  <= nums.length <= 1000 ``
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 262,621 | 143,160 | 54.5% |