### [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)

Hard

Given a string `` s `` representing a valid expression, implement a basic calculator to evaluate it, and return _the result of the evaluation_.

__Note:__ You are __not__ allowed to use any built-in function which evaluates strings as mathematical expressions, such as `` eval() ``.

 

<strong class="example">Example 1:</strong>

```
Input: s = "1 + 1"
Output: 2
```

<strong class="example">Example 2:</strong>

```
Input: s = " 2-1 + 2 "
Output: 3
```

<strong class="example">Example 3:</strong>

```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

 

__Constraints:__

*   <code>1 <= s.length <= 3 * 10<sup>5</sup></code>
*   `` s `` consists of digits, `` '+' ``, `` '-' ``, `` '(' ``, `` ')' ``, and `` ' ' ``.
*   `` s `` represents a valid expression.
*   `` '+' `` is __not__ used as a unary operation (i.e., `` "+1" `` and `` "+(2 + 3)" `` is invalid).
*   `` '-' `` could be used as a unary operation (i.e., `` "-1" `` and `` "-(2 + 3)" `` is valid).
*   There will be no two consecutive operators in the input.
*   Every number and running calculation will fit in a signed 32-bit integer.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 855,852 | 361,857 | 42.3% |