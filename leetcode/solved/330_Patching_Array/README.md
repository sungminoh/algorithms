### [330. Patching Array](https://leetcode.com/problems/patching-array/description/?envType=daily-question&envId=2024-06-16)

Hard

Given a sorted integer array `` nums `` and an integer `` n ``, add/patch elements to the array such that any number in the range `` [1, n] `` inclusive can be formed by the sum of some elements in the array.

Return _the minimum number of patches required_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,2,2], n = 5
Output: 0
```

 

__Constraints:__

*   `` 1 <= nums.length <= 1000 ``
*   <code>1 <= nums[i] <= 10<sup>4</sup></code>
*   `` nums `` is sorted in __ascending order__.
*   <code>1 <= n <= 2<sup>31</sup> - 1</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 293,828 | 155,875 | 53.0% |