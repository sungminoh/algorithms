### [2527. Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)

Hard

You are given an integer array `` nums `` and two integers `` minK `` and `` maxK ``.

A __fixed-bound subarray__ of `` nums `` is a subarray that satisfies the following conditions:

*   The __minimum__ value in the subarray is equal to `` minK ``.
*   The __maximum__ value in the subarray is equal to `` maxK ``.

Return _the __number__ of fixed-bound subarrays_.

A __subarray__ is a __contiguous__ part of an array.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i], minK, maxK <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 89,889 | 55,796 | 62.1% |