### [951. Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)

Medium

Given an integer array `` nums ``, partition it into two (contiguous) subarrays `` left `` and `` right `` so that:

*   Every element in `` left `` is less than or equal to every element in `` right ``.
*   `` left `` and `` right `` are non-empty.
*   `` left `` has the smallest possible size.

Return _the length of _`` left ``_ after such a partitioning_.

Test cases are generated such that partitioning exists.

 

__Example 1:__

```
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
```

__Example 2:__

```
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>5</sup></code>
*   <code>0 <= nums[i] <= 10<sup>6</sup></code>
*   There is at least one valid answer for the given input.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 117,899 | 56,138 | 47.6% |