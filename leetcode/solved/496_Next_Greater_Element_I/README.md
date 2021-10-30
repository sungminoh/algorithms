### [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

Easy

The __next greater element__ of some element `` x `` in an array is the __first greater__ element that is __to the right__ of `` x `` in the same array.

You are given two __distinct 0-indexed__ integer arrays `` nums1 `` and `` nums2 ``, where `` nums1 `` is a subset of `` nums2 ``.

For each `` 0 <= i < nums1.length ``, find the index `` j `` such that `` nums1[i] == nums2[j] `` and determine the __next greater element__ of `` nums2[j] `` in `` nums2 ``. If there is no next greater element, then the answer for this query is `` -1 ``.

Return _an array _`` ans ``_ of length _`` nums1.length ``_ such that _`` ans[i] ``_ is the __next greater element__ as described above._

 

__Example 1:__

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,<u>4</u>,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [<u>1</u>,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,<u>2</u>]. There is no next greater element, so the answer is -1.
```

__Example 2:__

```
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,<u>2</u>,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,<u>4</u>]. There is no next greater element, so the answer is -1.
```

 

__Constraints:__

*   `` 1 <= nums1.length <= nums2.length <= 1000 ``
*   <code>0 <= nums1[i], nums2[i] <= 10<sup>4</sup></code>
*   All integers in `` nums1 `` and `` nums2 `` are __unique__.
*   All the integers of `` nums1 `` also appear in `` nums2 ``.

 
__Follow up:__ Could you find an `` O(nums1.length + nums2.length) `` solution?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 415,481 | 284,960 | 68.6% |