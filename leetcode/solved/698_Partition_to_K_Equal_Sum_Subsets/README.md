### [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

Medium

Given an integer array `` nums `` and an integer `` k ``, return `` true `` if it is possible to divide this array into `` k `` non-empty subsets whose sums are all equal.

 

__Example 1:__

```
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```

__Example 2:__

```
Input: nums = [1,2,3,4], k = 3
Output: false
```

 

__Constraints:__

*   `` 1 <= k <= nums.length <= 16 ``
*   <code>1 <= nums[i] <= 10<sup>4</sup></code>
*   The frequency of each element is in the range `` [1, 4] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 357,900 | 163,675 | 45.7% |