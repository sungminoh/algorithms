### [2530. Minimize Maximum of Array](https://leetcode.com/problems/minimize-maximum-of-array/)

Medium

You are given a __0-indexed__ array `` nums `` comprising of `` n `` non-negative integers.

In one operation, you must:

*   Choose an integer `` i `` such that `` 1 <= i < n `` and `` nums[i] > 0 ``.
*   Decrease `` nums[i] `` by 1.
*   Increase `` nums[i - 1] `` by 1.

Return_ the __minimum__ possible value of the __maximum__ integer of _`` nums ``_ after performing __any__ number of operations_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>2 <= n <= 10<sup>5</sup></code>
*   <code>0 <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 154,755 | 72,776 | 47.0% |