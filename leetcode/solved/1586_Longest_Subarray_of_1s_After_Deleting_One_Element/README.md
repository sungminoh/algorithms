### [1586. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24)

Medium

Given a binary array `` nums ``, you should delete one element from it.

Return _the size of the longest non-empty subarray containing only _`` 1 ``_'s in the resulting array_. Return `` 0 `` if there is no such subarray.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   `` nums[i] `` is either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 800,601 | 567,186 | 70.8% |