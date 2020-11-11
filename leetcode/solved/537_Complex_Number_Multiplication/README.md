### [537. Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/)

Medium

Given two strings representing two [complex numbers](https://en.wikipedia.org/wiki/Complex_number).

You need to return a string representing their multiplication. Note i<sup>2</sup> = -1 according to the definition.

__Example 1:__  

```
<b>Input:</b> "1+1i", "1+1i"
<b>Output:</b> "0+2i"
<b>Explanation:</b> (1 + i) * (1 + i) = 1 + i<sup>2</sup> + 2 * i = 2i, and you need convert it to the form of 0+2i.
```

__Example 2:__  

```
<b>Input:</b> "1+-1i", "1+-1i"
<b>Output:</b> "0+-2i"
<b>Explanation:</b> (1 - i) * (1 - i) = 1 + i<sup>2</sup> - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```

__Note:__

1.   The input strings will not have extra blank.
2.   The input strings will be given in the form of __a+bi__, where the integer __a__ and __b__ will both belong to the range of \[-100, 100\]. And __the output should be also in this form__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 68,506 | 45,919 | 67.0% |