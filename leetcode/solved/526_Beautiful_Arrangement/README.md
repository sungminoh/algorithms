### [526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)

Medium

Suppose you have `` n `` integers labeled `` 1 `` through `` n ``. A permutation of those `` n `` integers `` perm `` (__1-indexed__) is considered a __beautiful arrangement__ if for every `` i `` (`` 1 <= i <= n ``), __either__ of the following is true:

*   `` perm[i] `` is divisible by `` i ``.
*   `` i `` is divisible by `` perm[i] ``.

Given an integer `` n ``, return _the __number__ of the __beautiful arrangements__ that you can construct_.

 

__Example 1:__

```
Input: n = 2
Output: 2
<b>Explanation:</b> 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
```

__Example 2:__

```
Input: n = 1
Output: 1
```

 

__Constraints:__

*   `` 1 <= n <= 15 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 146,148 | 90,889 | 62.2% |