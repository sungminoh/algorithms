### [537. Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/)

Medium

A <a href="https://en.wikipedia.org/wiki/Complex_number" target="_blank">complex number</a> can be represented as a string on the form <code>"<strong>real</strong>+<strong>imaginary</strong>i"</code> where:

*   `` real `` is the real part and is an integer in the range `` [-100, 100] ``.
*   `` imaginary `` is the imaginary part and is an integer in the range `` [-100, 100] ``.
*   <code>i<sup>2</sup> == -1</code>.

Given two complex numbers `` num1 `` and `` num2 `` as strings, return _a string of the complex number that represents their multiplications_.

 

__Example 1:__

```
Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
```

__Example 2:__

```
Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```

 

__Constraints:__

*   `` num1 `` and `` num2 `` are valid complex numbers.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 107,589 | 76,231 | 70.9% |