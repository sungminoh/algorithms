### [954. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

Medium

Given a __circular integer array__ `` nums `` of length `` n ``, return _the maximum possible sum of a non-empty __subarray__ of _`` nums ``.

A __circular array__ means the end of the array connects to the beginning of the array. Formally, the next element of `` nums[i] `` is `` nums[(i + 1) % n] `` and the previous element of `` nums[i] `` is `` nums[(i - 1 + n) % n] ``.

A __subarray__ may only include each element of the fixed buffer `` nums `` at most once. Formally, for a subarray `` nums[i], nums[i + 1], ..., nums[j] ``, there does not exist `` i <= k1 ``, `` k2 <= j `` with `` k1 % n == k2 % n ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>1 <= n <= 3 * 10<sup>4</sup></code>
*   <code>-3 * 10<sup>4</sup> <= nums[i] <= 3 * 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 473,587 | 202,888 | 42.8% |