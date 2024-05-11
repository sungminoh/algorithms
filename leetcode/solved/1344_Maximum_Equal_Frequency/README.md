### [1344. Maximum Equal Frequency](https://leetcode.com/problems/maximum-equal-frequency/description/)

Hard

Given an array `` nums `` of positive integers, return the longest possible length of an array prefix of `` nums ``, such that it is possible to remove __exactly one__ element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 40,155 | 14,888 | 37.1% |