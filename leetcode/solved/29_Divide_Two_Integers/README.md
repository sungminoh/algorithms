### [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Medium

Given two integers `` dividend `` and `` divisor ``, divide two integers __without__ using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, `` 8.345 `` would be truncated to `` 8 ``, and `` -2.7335 `` would be truncated to `` -2 ``.

Return _the __quotient__ after dividing _`` dividend ``_ by _`` divisor ``.

__Note: __Assume we are dealing with an environment that could only store integers within the __32-bit__ signed integer range: <code>[−2<sup>31</sup>, 2<sup>31</sup> − 1]</code>. For this problem, if the quotient is __strictly greater than__ <code>2<sup>31</sup> - 1</code>, then return <code>2<sup>31</sup> - 1</code>, and if the quotient is __strictly less than__ <code>-2<sup>31</sup></code>, then return <code>-2<sup>31</sup></code>.

 

__Example 1:__

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
```

__Example 2:__

```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
```

 

__Constraints:__

*   <code>-2<sup>31</sup> <= dividend, divisor <= 2<sup>31</sup> - 1</code>
*   `` divisor != 0 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,921,294 | 511,350 | 17.5% |