### [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/description/?envType=daily-question&envId=2023-11-29)

Easy

Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).

__Note:__

*   Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
*   In Java, the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2's complement notation</a>. Therefore, in <strong class="example">Example 3</strong>, the input represents the signed integer. `` -3 ``.

 

<strong class="example">Example 1:</strong>

```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

<strong class="example">Example 2:</strong>

```
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```

<strong class="example">Example 3:</strong>

```
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

 

__Constraints:__

*   The input must be a __binary string__ of length `` 32 ``.

 
__Follow up:__ If this function is called many times, how would you optimize it?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,966,159 | 1,380,050 | 70.2% |