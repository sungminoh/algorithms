### [1800. Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)

Medium

Given an integer `` n ``, return _the __decimal value__ of the binary string formed by concatenating the binary representations of _`` 1 ``_ to _`` n ``_ in order, __modulo ___<code>10<sup>9 </sup>+ 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
```

<strong class="example">Example 2:</strong>

```
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
```

<strong class="example">Example 3:</strong>

```
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10<sup>9</sup> + 7, the result is 505379714.
```

 

__Constraints:__

*   <code>1 <= n <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 147,799 | 84,296 | 57.0% |