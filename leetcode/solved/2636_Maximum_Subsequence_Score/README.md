### [2636. Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/?envType=daily-question&envId=2023-05-24)

Medium

You are given two __0-indexed__ integer arrays `` nums1 `` and `` nums2 `` of equal length `` n `` and a positive integer `` k ``. You must choose a __subsequence__ of indices from `` nums1 `` of length `` k ``.

For chosen indices <code>i<sub>0</sub></code>, <code>i<sub>1</sub></code>, ..., <code>i<sub>k - 1</sub></code>, your __score__ is defined as:

*   The sum of the selected elements from `` nums1 `` multiplied with the __minimum__ of the selected elements from `` nums2 ``.
*   It can defined simply as: <code>(nums1[i<sub>0</sub>] + nums1[i<sub>1</sub>] +...+ nums1[i<sub>k - 1</sub>]) * min(nums2[i<sub>0</sub>] , nums2[i<sub>1</sub>], ... ,nums2[i<sub>k - 1</sub>])</code>.

Return _the __maximum__ possible score._

A __subsequence__ of indices of an array is a set that can be derived from the set `` {0, 1, ..., n-1} `` by deleting some or no elements.

 

<strong class="example">Example 1:</strong>

```
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
```

<strong class="example">Example 2:</strong>

```
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
```

 

__Constraints:__

*   `` n == nums1.length == nums2.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>0 <= nums1[i], nums2[j] <= 10<sup>5</sup></code>
*   `` 1 <= k <= n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 113,233 | 62,295 | 55.0% |