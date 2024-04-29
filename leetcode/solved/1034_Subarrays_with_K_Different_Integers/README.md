### [1034. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/description/)

Hard

Given an integer array `` nums `` and an integer `` k ``, return _the number of __good subarrays__ of _`` nums ``.

A __good array__ is an array where the number of different integers in that array is exactly `` k ``.

*   For example, `` [1,2,3,1,2] `` has `` 3 `` different integers: `` 1 ``, `` 2 ``, and `` 3 ``.

A __subarray__ is a __contiguous__ part of an array.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
```

 

__Constraints:__

*   <code>1 <= nums.length <= 2 * 10<sup>4</sup></code>
*   `` 1 <= nums[i], k <= nums.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 328,955 | 207,324 | 63.0% |