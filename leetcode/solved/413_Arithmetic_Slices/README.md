### [413. Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/)

Medium

An integer array is called arithmetic if it consists of __at least three elements__ and if the difference between any two consecutive elements is the same.

*   For example, `` [1,3,5,7,9] ``, `` [7,7,7,7] ``, and `` [3,-1,-5,-9] `` are arithmetic sequences.

Given an integer array `` nums ``, return _the number of arithmetic __subarrays__ of_ `` nums ``.

A __subarray__ is a contiguous subsequence of the array.

 

__Example 1:__

```
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
```

__Example 2:__

```
Input: nums = [1]
Output: 0
```

 

__Constraints:__

*   `` 1 <= nums.length <= 5000 ``
*   `` -1000 <= nums[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 341,387 | 219,271 | 64.2% |