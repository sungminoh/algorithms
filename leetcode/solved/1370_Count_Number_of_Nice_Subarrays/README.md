### [1370. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=daily-question&envId=2024-06-22)

Medium

Given an array of integers `` nums `` and an integer `` k ``. A continuous subarray is called __nice__ if there are `` k `` odd numbers on it.

Return _the number of __nice__ sub-arrays_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
```

<strong class="example">Example 2:</strong>

```
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
```

 

__Constraints:__

*   `` 1 <= nums.length <= 50000 ``
*   `` 1 <= nums[i] <= 10^5 ``
*   `` 1 <= k <= nums.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 349,827 | 248,021 | 70.9% |