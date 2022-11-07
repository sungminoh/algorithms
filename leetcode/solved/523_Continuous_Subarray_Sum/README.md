### [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/submissions/)

Medium

Given an integer array nums and an integer k, return `` true `` _if _`` nums ``_ has a __good subarray__ or _`` false ``_ otherwise_.

A __good subarray__ is a subarray where:

*   its length is __at least two__, and
*   the sum of the elements of the subarray is a multiple of `` k ``.

__Note__ that:

*   A __subarray__ is a contiguous part of the array.
*   An integer `` x `` is a multiple of `` k `` if there exists an integer `` n `` such that `` x = n * k ``. `` 0 `` is __always__ a multiple of `` k ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [23,<u>2,4</u>,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [<u>23,2,6,4,7</u>], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [23,2,6,4,7], k = 13
Output: false
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>0 <= nums[i] <= 10<sup>9</sup></code>
*   <code>0 <= sum(nums[i]) <= 2<sup>31</sup> - 1</code>
*   <code>1 <= k <= 2<sup>31</sup> - 1</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,305,125 | 372,398 | 28.5% |