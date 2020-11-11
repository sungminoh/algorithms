### [872. Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)

Medium

Given a string `` S `` of digits, such as `` S = "123456579" ``, we can split it into a _Fibonacci-like sequence_ `` [123, 456, 579]. ``

Formally, a Fibonacci-like sequence is a list `` F `` of non-negative integers such that:

*   `` 0 <= F[i] <= 2^31 - 1 ``, (that is, each integer fits a 32-bit signed integer type);
*   `` F.length >= 3 ``;
*   and``  F[i] + F[i+1] = F[i+2]  ``for all `` 0 <= i < F.length - 2 ``.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from `` S ``, or return `` [] `` if it cannot be done.

__Example 1:__

```
Input: "123456579"
Output: [123,456,579]
```

__Example 2:__

```
Input: "11235813"
Output: [1,1,2,3,5,8,13]
```

__Example 3:__

```
Input: "112358130"
Output: []
Explanation: The task is impossible.
```

__Example 4:__

```
Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
```

__Example 5:__

```
Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
```

__Note: __

1.   `` 1 <= S.length <= 200 ``
2.   `` S `` contains only digits.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 58,093 | 21,126 | 36.4% |