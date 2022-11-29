### [689. Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)

Hard

Given an integer array `` nums `` and an integer `` k ``, find three non-overlapping subarrays of length `` k `` with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (__0-indexed__). If there are multiple answers, return the lexicographically smallest one.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
```

 

__Constraints:__

*   <code>1 <= nums.length <= 2 * 10<sup>4</sup></code>
*   <code>1 <= nums[i] < 2<sup>16</sup></code>
*   `` 1 <= k <= floor(nums.length / 3) ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 134,280 | 65,650 | 48.9% |