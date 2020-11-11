### [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

Medium

Given a sorted array `` arr ``, two integers `` k `` and `` x ``, find the `` k `` closest elements to `` x `` in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

__Example 1:__

```Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

__Example 2:__

```Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
```

 

__Constraints:__

*   `` 1 <= k <= arr.length ``
*   `` 1 <= arr.length <= 10^4 ``
*   Absolute value of elements in the array and `` x `` will not exceed 10<sup>4</sup>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 255,452 | 103,862 | 40.7% |