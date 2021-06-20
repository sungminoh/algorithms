### [1807. Partitioning Into Minimum Number Of Deci-Binary Numbers](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)

Medium

A decimal number is called __deci-binary__ if each of its digits is either `` 0 `` or `` 1 `` without any leading zeros. For example, `` 101 `` and `` 1100 `` are __deci-binary__, while `` 112 `` and `` 3001 `` are not.

Given a string `` n `` that represents a positive decimal integer, return _the __minimum__ number of positive __deci-binary__ numbers needed so that they sum up to _`` n ``_._

 

__Example 1:__

```
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
```

__Example 2:__

```
Input: n = "82734"
Output: 8
```

__Example 3:__

```
Input: n = "27346209830709182346"
Output: 9
```

 

__Constraints:__

*   <code>1 <= n.length <= 10<sup>5</sup></code>
*   `` n `` consists of only digits.
*   `` n `` does not contain any leading zeros and represents a positive integer.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 51,905 | 46,079 | 88.8% |