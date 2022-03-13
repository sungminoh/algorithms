### [338. Counting Bits](https://leetcode.com/problems/counting-bits/)

Easy

Given an integer `` n ``, return _an array _`` ans ``_ of length _`` n + 1 ``_ such that for each _`` i ``_ _(`` 0 <= i <= n ``)_, _`` ans[i] ``_ is the __number of ___`` 1 ``___'s__ in the binary representation of _`` i ``.

 

__Example 1:__

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

__Example 2:__

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

 

__Constraints:__

*   <code>0 <= n <= 10<sup>5</sup></code>

 

__Follow up:__

*   It is very easy to come up with a solution with a runtime of `` O(n log n) ``. Can you do it in linear time `` O(n) `` and possibly in a single pass?
*   Can you do it without using any built-in function (i.e., like `` __builtin_popcount `` in C++)?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 732,622 | 542,100 | 74.0% |