### [1925. Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array/description/?envType=daily-question&envId=2023-11-21)

Medium

You are given an array `` nums `` that consists of non-negative integers. Let us define `` rev(x) `` as the reverse of the non-negative integer `` x ``. For example, `` rev(123) = 321 ``, and `` rev(120) = 21 ``. A pair of indices `` (i, j) `` is __nice__ if it satisfies all of the following conditions:

*   `` 0 <= i < j < nums.length ``
*   `` nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) ``

Return _the number of nice pairs of indices_. Since that number can be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [13,10,35,24,76]
Output: 4
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>0 <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 208,851 | 102,858 | 49.2% |