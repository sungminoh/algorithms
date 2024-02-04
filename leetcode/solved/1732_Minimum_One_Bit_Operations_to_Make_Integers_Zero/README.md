### [1732. Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2023-11-30)

Hard

Given an integer `` n ``, you must transform it into `` 0 `` using the following operations any number of times:

*   Change the rightmost (<code>0<sup>th</sup></code>) bit in the binary representation of `` n ``.
*   Change the <code>i<sup>th</sup></code> bit in the binary representation of `` n `` if the <code>(i-1)<sup>th</sup></code> bit is set to `` 1 `` and the <code>(i-2)<sup>th</sup></code> through <code>0<sup>th</sup></code> bits are set to `` 0 ``.

Return _the minimum number of operations to transform _`` n ``_ into _`` 0 ``_._

 

<strong class="example">Example 1:</strong>

```
Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"<u>1</u>1" -> "<u>0</u>1" with the 2<sup>nd</sup> operation since the 0<sup>th</sup> bit is 1.
"0<u>1</u>" -> "0<u>0</u>" with the 1<sup>st</sup> operation.
```

<strong class="example">Example 2:</strong>

```
Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"<u>1</u>10" -> "<u>0</u>10" with the 2<sup>nd</sup> operation since the 1<sup>st</sup> bit is 1 and 0<sup>th</sup> through 0<sup>th</sup> bits are 0.
"01<u>0</u>" -> "01<u>1</u>" with the 1<sup>st</sup> operation.
"0<u>1</u>1" -> "0<u>0</u>1" with the 2<sup>nd</sup> operation since the 0<sup>th</sup> bit is 1.
"00<u>1</u>" -> "00<u>0</u>" with the 1<sup>st</sup> operation.
```

 

__Constraints:__

*   <code>0 <= n <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 75,548 | 56,354 | 74.6% |