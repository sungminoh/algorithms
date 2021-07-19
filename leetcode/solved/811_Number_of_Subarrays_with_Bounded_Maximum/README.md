### [811. Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/)

Medium

Given an integer array `` nums `` and two integers `` left `` and `` right ``, return _the number of contiguous non-empty __subarrays__ such that the value of the maximum array element in that subarray is in the range _`` [left, right] ``.

The test cases are generated so that the answer will fit in a __32-bit__ integer.

 

__Example 1:__

```
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```

__Example 2:__

```
Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>0 <= nums[i] <= 10<sup>9</sup></code>
*   <code>0 <= left <= right <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 83,401 | 43,172 | 51.8% |