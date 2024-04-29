### [1037. Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/)

Hard

You are given a binary array `` nums `` and an integer `` k ``.

A __k-bit flip__ is choosing a __subarray__ of length `` k `` from `` nums `` and simultaneously changing every `` 0 `` in the subarray to `` 1 ``, and every `` 1 `` in the subarray to `` 0 ``.

Return _the minimum number of __k-bit flips__ required so that there is no _`` 0 ``_ in the array_. If it is not possible, return `` -1 ``.

A __subarray__ is a __contiguous__ part of an array.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
```

<strong class="example">Example 3:</strong>

```
Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   `` 1 <= k <= nums.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 67,274 | 34,671 | 51.5% |