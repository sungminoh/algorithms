### [792. Binary Search](https://leetcode.com/problems/binary-search/)

Easy

Given an array of integers `` nums `` which is sorted in ascending order, and an integer `` target ``, write a function to search `` target `` in `` nums ``. If `` target `` exists, then return its index. Otherwise, return `` -1 ``.

You must write an algorithm with `` O(log n) `` runtime complexity.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

<strong class="example">Example 2:</strong>

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> < nums[i], target < 10<sup>4</sup></code>
*   All the integers in `` nums `` are __unique__.
*   `` nums `` is sorted in ascending order.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 3,117,620 | 1,751,413 | 56.2% |