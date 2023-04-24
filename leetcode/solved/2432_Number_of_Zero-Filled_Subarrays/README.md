### [2432. Number of Zero-Filled Subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays/)

Medium

Given an integer array `` nums ``, return _the number of __subarrays__ filled with _`` 0 ``.

A __subarray__ is a contiguous non-empty sequence of elements within an array.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 158,846 | 106,012 | 66.7% |