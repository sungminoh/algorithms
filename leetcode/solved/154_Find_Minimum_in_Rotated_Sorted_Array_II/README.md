### [154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

Hard

Suppose an array of length `` n `` sorted in ascending order is __rotated__ between `` 1 `` and `` n `` times. For example, the array `` nums = [0,1,4,4,5,6,7] `` might become:

*   `` [4,5,6,7,0,1,4] `` if it was rotated `` 4 `` times.
*   `` [0,1,4,4,5,6,7] `` if it was rotated `` 7 `` times.

Notice that __rotating__ an array `` [a[0], a[1], a[2], ..., a[n-1]] `` 1 time results in the array `` [a[n-1], a[0], a[1], a[2], ..., a[n-2]] ``.

Given the sorted rotated array `` nums `` that may contain __duplicates__, return _the minimum element of this array_.

You must decrease the overall operation steps as much as possible.

 

__Example 1:__

```Input: nums = [1,3,5]
Output: 1
```

__Example 2:__

```Input: nums = [2,2,2,0,1]
Output: 0
```

 

__Constraints:__

*   `` n == nums.length ``
*   `` 1 <= n <= 5000 ``
*   `` -5000 <= nums[i] <= 5000 ``
*   `` nums `` is sorted and rotated between `` 1 `` and `` n `` times.

 

__Follow up:__ This problem is similar to <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/" target="_blank">Find Minimum in Rotated Sorted Array</a>, but `` nums `` may contain __duplicates__. Would this affect the runtime complexity? How and why?

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 679,513 | 293,278 | 43.2% |