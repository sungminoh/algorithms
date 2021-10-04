### [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)

Hard

Given a string `` s `` representing a valid expression, implement a basic calculator to evaluate it, and return _the result of the evaluation_.

__Note:__ You are __not__ allowed to use any built-in function which evaluates strings as mathematical expressions, such as `` eval() ``.

 

__Example 1:__

```
Input: s = "1 + 1"
Output: 2
```

__Example 2:__

```
Input: s = " 2-1 + 2 "
Output: 3
```

__Example 3:__

```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

 

__Constraints:__

*   <code>1 <= s.length <= 3 * 10<sup>5</sup></code>
*   `` s `` consists of digits, `` '+' ``, `` '-' ``, `` '(' ``, `` ')' ``, and `` ' ' ``.
*   `` s `` represents a valid expression.
*   `` '+' `` is not used as a unary operation.
*   `` '-' `` could be used as a unary operation and in this case, it will not be used directly after a +ve or -ve signs (will be inside parentheses).
*   There will be no two consecutive operators in the input.
*   Every number and running calculation will fit in a signed 32-bit integer.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 630,692 | 248,399 | 39.4% |