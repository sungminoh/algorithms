### [1064. Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/)

Medium

Given a positive integer `` k ``, you need to find the __length__ of the __smallest__ positive integer `` n `` such that `` n `` is divisible by `` k ``, and `` n `` only contains the digit `` 1 ``.

Return _the __length__ of _`` n ``. If there is no such `` n ``, return -1.

__Note:__ `` n `` may not fit in a 64-bit signed integer.

 

__Example 1:__

```
Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
```

__Example 2:__

```
Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
```

__Example 3:__

```
Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
```

 

__Constraints:__

*   <code>1 <= k <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 113,077 | 52,978 | 46.9% |