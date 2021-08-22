### [1046. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

Medium

Given a binary array `` nums `` and an integer `` k ``, return _the maximum number of consecutive _`` 1 ``_'s in the array if you can flip at most_ `` k `` `` 0 ``'s.

 

__Example 1:__

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,<u>1,1,1,1,1,1</u>]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

__Example 2:__

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,<u>1,1,1,1,1,1,1,1,1,1</u>,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   `` nums[i] `` is either `` 0 `` or `` 1 ``.
*   `` 0 <= k <= nums.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 229,101 | 139,859 | 61.0% |