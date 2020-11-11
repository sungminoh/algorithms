### [321. Create Maximum Number](https://leetcode.com/problems/create-maximum-number/)

Hard

Given two arrays of length `` m `` and `` n `` with digits `` 0-9 `` representing two numbers. Create the maximum number of length `` k <= m + n `` from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the `` k `` digits.

__Note: __You should try to optimize your time and space complexity.

__Example 1:__

<strong>Input:</strong>
    nums1 = [3, 4, 6, 5]
    nums2 = <code>[9, 1, 2, 5, 8, 3]</code>
    k = <code>5</code>
<strong>Output:</strong>
<code>[9, 8, 6, 5, 3]</code>

__Example 2:__

<strong>Input:</strong>
    nums1 = [6, 7]
    nums2 = <code>[6, 0, 4]</code>
    k = <code>5</code>
<strong>Output:</strong>
<code>[6, 7, 6, 0, 4]</code>

__Example 3:__

<strong>Input:</strong>
    nums1 = [3, 9]
    nums2 = <code>[8, 9]</code>
    k = <code>3</code>
<strong>Output:</strong>
<code>[9, 8, 9]</code> 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 142,194 | 37,974 | 26.7% |