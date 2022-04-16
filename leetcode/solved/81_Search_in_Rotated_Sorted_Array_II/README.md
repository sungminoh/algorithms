### [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

Medium

There is an integer array `` nums `` sorted in non-decreasing order (not necessarily with __distinct__ values).

Before being passed to your function, `` nums `` is __rotated__ at an unknown pivot index `` k `` (`` 0 <= k < nums.length ``) such that the resulting array is `` [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] `` (__0-indexed__). For example, `` [0,1,2,4,4,4,5,6,6,7] `` might be rotated at pivot index `` 5 `` and become `` [4,5,6,6,7,0,1,2,4,4] ``.

Given the array `` nums `` __after__ the rotation and an integer `` target ``, return `` true ``_ if _`` target ``_ is in _`` nums ``_, or _`` false ``_ if it is not in _`` nums ``_._

You must decrease the overall operation steps as much as possible.

 

__Example 1:__

```Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

__Example 2:__

```Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

 

__Constraints:__

*   `` 1 <= nums.length <= 5000 ``
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   `` nums `` is guaranteed to be rotated at some pivot.
*   <code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code>

 

__Follow up:__ This problem is similar to <a href="/problems/search-in-rotated-sorted-array/description/" target="_blank">Search in Rotated Sorted Array</a>, but `` nums `` may contain __duplicates__. Would this affect the runtime complexity? How and why?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,178,671 | 418,976 | 35.5% |