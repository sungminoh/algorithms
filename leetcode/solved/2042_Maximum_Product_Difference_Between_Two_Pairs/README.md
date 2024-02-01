### [2042. Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/?envType=daily-question&envId=2023-12-18)

Easy

The __product difference__ between two pairs `` (a, b) `` and `` (c, d) `` is defined as `` (a * b) - (c * d) ``.

*   For example, the product difference between `` (5, 6) `` and `` (2, 7) `` is `` (5 * 6) - (2 * 7) = 16 ``.

Given an integer array `` nums ``, choose four __distinct__ indices `` w ``, `` x ``, `` y ``, and `` z `` such that the __product difference__ between pairs `` (nums[w], nums[x]) `` and `` (nums[y], nums[z]) `` is __maximized__.

Return _the __maximum__ such product difference_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
```

 

__Constraints:__

*   <code>4 <= nums.length <= 10<sup>4</sup></code>
*   <code>1 <= nums[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 270,052 | 223,860 | 82.9% |