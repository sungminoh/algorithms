### [89. Gray Code](https://leetcode.com/problems/gray-code/)

Medium

An __n-bit gray code sequence__ is a sequence of <code>2<sup>n</sup></code> integers where:

*   Every integer is in the __inclusive__ range <code>[0, 2<sup>n</sup> - 1]</code>,
*   The first integer is `` 0 ``,
*   An integer appears __no more than once__ in the sequence,
*   The binary representation of every pair of __adjacent__ integers differs by __exactly one bit__, and
*   The binary representation of the __first__ and __last__ integers differs by __exactly one bit__.

Given an integer `` n ``, return _any valid __n-bit gray code sequence___.

 

__Example 1:__

```
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 0<u>0</u> and 0<u>1</u> differ by one bit
- <u>0</u>1 and <u>1</u>1 differ by one bit
- 1<u>1</u> and 1<u>0</u> differ by one bit
- <u>1</u>0 and <u>0</u>0 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- <u>0</u>0 and <u>1</u>0 differ by one bit
- 1<u>0</u> and 1<u>1</u> differ by one bit
- <u>1</u>1 and <u>0</u>1 differ by one bit
- 0<u>1</u> and 0<u>0</u> differ by one bit
```

__Example 2:__

```
Input: n = 1
Output: [0,1]
```

 

__Constraints:__

*   `` 1 <= n <= 16 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 396,474 | 212,835 | 53.7% |