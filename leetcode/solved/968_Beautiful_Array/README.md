### [968. Beautiful Array](https://leetcode.com/problems/beautiful-array/)

Medium

An array `` nums `` of length `` n `` is __beautiful__ if:

*   `` nums `` is a permutation of the integers in the range `` [1, n] ``.
*   For every `` 0 <= i < j < n ``, there is no index `` k `` with `` i < k < j `` where `` 2 * nums[k] == nums[i] + nums[j] ``.

Given the integer `` n ``, return _any __beautiful__ array _`` nums ``_ of length _`` n ``. There will be at least one valid answer for the given `` n ``.

 

__Example 1:__

```Input: n = 4
Output: [2,1,4,3]
```

__Example 2:__

```Input: n = 5
Output: [3,1,2,5,4]
```

 

__Constraints:__

*   `` 1 <= n <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 48,651 | 30,807 | 63.3% |