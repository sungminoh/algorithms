### [1016. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

Medium

Given an integer array `` nums `` and an integer `` k ``, return _the number of non-empty __subarrays__ that have a sum divisible by _`` k ``.

A __subarray__ is a __contiguous__ part of an array.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

<strong class="example">Example 2:</strong>

```
Input: nums = [5], k = 9
Output: 0
```

 

__Constraints:__

*   <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   <code>2 <= k <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 353,060 | 192,342 | 54.5% |