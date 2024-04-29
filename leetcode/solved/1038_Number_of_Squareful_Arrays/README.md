### [1038. Number of Squareful Arrays](https://leetcode.com/problems/number-of-squareful-arrays/description/)

Hard

An array is __squareful__ if the sum of every pair of adjacent elements is a __perfect square__.

Given an integer array nums, return _the number of permutations of _`` nums ``_ that are __squareful___.

Two permutations `` perm1 `` and `` perm2 `` are different if there is some index `` i `` such that `` perm1[i] != perm2[i] ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [2,2,2]
Output: 1
```

 

__Constraints:__

*   `` 1 <= nums.length <= 12 ``
*   <code>0 <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 77,559 | 38,863 | 50.1% |