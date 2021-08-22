### [899. Binary Gap](https://leetcode.com/problems/binary-gap/)

Easy

Given a positive integer `` n ``, find and return _the __longest distance__ between any two __adjacent__ _`` 1 ``_'s in the binary representation of _`` n ``_. If there are no two adjacent _`` 1 ``_'s, return _`` 0 ``_._

Two `` 1 ``'s are __adjacent__ if there are only `` 0 ``'s separating them (possibly no `` 0 ``'s). The __distance__ between two `` 1 ``'s is the absolute difference between their bit positions. For example, the two `` 1 ``'s in `` "1001" `` have a distance of 3.

 

__Example 1:__

```
Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "<u>1</u>0<u>1</u>10" with a distance of 2.
The second adjacent pair of 1's is "10<u>11</u>0" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "<u>1</u>01<u>1</u>0" is not a valid pair since there is a 1 separating the two 1's underlined.
```

__Example 2:__

```
Input: n = 5
Output: 2
Explanation: 5 in binary is "101".
```

__Example 3:__

```
Input: n = 6
Output: 1
Explanation: 6 in binary is "110".
```

__Example 4:__

```
Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There aren't any adjacent pairs of 1's in the binary representation of 8, so we return 0.
```

__Example 5:__

```
Input: n = 1
Output: 0
```

 

__Constraints:__

*   <code>1 <= n <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 82,643 | 50,744 | 61.4% |