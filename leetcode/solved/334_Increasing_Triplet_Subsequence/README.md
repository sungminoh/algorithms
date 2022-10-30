### [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)

Medium

Given an integer array `` nums ``, return `` true ``_ if there exists a triple of indices _`` (i, j, k) ``_ such that _`` i < j < k ``_ and _`` nums[i] < nums[j] < nums[k] ``. If no such indices exists, return `` false ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 5 * 10<sup>5</sup></code>
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>

 
__Follow up:__ Could you implement a solution that runs in `` O(n) `` time complexity and `` O(1) `` space complexity?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 843,598 | 360,112 | 42.7% |