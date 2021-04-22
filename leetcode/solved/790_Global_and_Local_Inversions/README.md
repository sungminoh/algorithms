### [790. Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/)

Medium

You are given an integer array `` nums `` of length `` n `` which represents a permutation of all the integers in the range `` [0, n - 1] ``.

The number of __global inversions__ is the number of the different pairs `` (i, j) `` where:

*   `` 0 <= i < j < n ``
*   `` nums[i] > nums[j] ``

The number of __local inversions__ is the number of indices `` i `` where:

*   `` 0 <= i < n - 1 ``
*   `` nums[i] > nums[i + 1] ``

Return `` true `` _if the number of __global inversions__ is equal to the number of __local inversions___.

 

__Example 1:__

```
Input: nums = [1,0,2]
Output: true
Explanation: There is 1 global inversion and 1 local inversion.
```

__Example 2:__

```
Input: nums = [1,2,0]
Output: false
Explanation: There are 2 global inversions and 1 local inversion.
```

 

__Constraints:__

*   `` n == nums.length ``
*   `` 1 <= n <= 5000 ``
*   `` 0 <= nums[i] < n ``
*   All the integers of `` nums `` are __unique__.
*   `` nums `` is a permutation of all the numbers in the range `` [0, n - 1] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 101,824 | 47,075 | 46.2% |