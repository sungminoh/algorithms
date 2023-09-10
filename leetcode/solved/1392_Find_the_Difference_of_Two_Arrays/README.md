### [1392. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=daily-question&envId=2023-05-03)

Easy

Given two __0-indexed__ integer arrays `` nums1 `` and `` nums2 ``, return _a list_ `` answer `` _of size_ `` 2 `` _where:_

*   `` answer[0] `` _is a list of all __distinct__ integers in_ `` nums1 `` _which are __not__ present in_ `` nums2 ``_._
*   `` answer[1] `` _is a list of all __distinct__ integers in_ `` nums2 `` _which are __not__ present in_ `` nums1 ``.

__Note__ that the integers in the lists may be returned in __any__ order.

 

<strong class="example">Example 1:</strong>

```
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
```

<strong class="example">Example 2:</strong>

```
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
```

 

__Constraints:__

*   `` 1 <= nums1.length, nums2.length <= 1000 ``
*   `` -1000 <= nums1[i], nums2[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 243,750 | 191,115 | 78.4% |