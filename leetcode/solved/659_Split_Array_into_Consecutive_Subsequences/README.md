### [659. Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)

Medium

You are given an integer array `` nums `` that is __sorted in non-decreasing order__.

Determine if it is possible to split `` nums `` into __one or more subsequences__ such that __both__ of the following conditions are true:

*   Each subsequence is a __consecutive increasing sequence__ (i.e. each integer is __exactly one__ more than the previous integer).
*   All subsequences have a length of `` 3 ``__ or more__.

Return `` true ``_ if you can split _`` nums ``_ according to the above conditions, or _`` false ``_ otherwise_.

A __subsequence__ of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., `` [1,3,5] `` is a subsequence of <code>[<u>1</u>,2,<u>3</u>,4,<u>5</u>]</code> while `` [1,3,2] `` is not).

 

__Example 1:__

```
Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[<u>1</u>,<u>2</u>,<u>3</u>,3,4,5] --> 1, 2, 3
[1,2,3,<u>3</u>,<u>4</u>,<u>5</u>] --> 3, 4, 5
```

__Example 2:__

```
Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[<u>1</u>,<u>2</u>,<u>3</u>,3,<u>4</u>,4,<u>5</u>,5] --> 1, 2, 3, 4, 5
[1,2,3,<u>3</u>,4,<u>4</u>,5,<u>5</u>] --> 3, 4, 5
```

__Example 3:__

```
Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   `` -1000 <= nums[i] <= 1000 ``
*   `` nums `` is sorted in __non-decreasing__ order.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 228,174 | 115,234 | 50.5% |