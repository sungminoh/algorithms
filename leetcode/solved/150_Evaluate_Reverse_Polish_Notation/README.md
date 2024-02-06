### [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30)

Medium

You are given an array of strings `` tokens `` that represents an arithmetic expression in a <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.

Evaluate the expression. Return _an integer that represents the value of the expression_.

__Note__ that:

*   The valid operators are `` '+' ``, `` '-' ``, `` '*' ``, and `` '/' ``.
*   Each operand may be an integer or another expression.
*   The division between two integers always __truncates toward zero__.
*   There will not be any division by zero.
*   The input represents a valid arithmetic expression in a reverse polish notation.
*   The answer and all the intermediate calculations can be represented in a __32-bit__ integer.

 

<strong class="example">Example 1:</strong>

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

<strong class="example">Example 2:</strong>

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

<strong class="example">Example 3:</strong>

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

 

__Constraints:__

*   <code>1 <= tokens.length <= 10<sup>4</sup></code>
*   `` tokens[i] `` is either an operator: `` "+" ``, `` "-" ``, `` "*" ``, or `` "/" ``, or an integer in the range `` [-200, 200] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,887,241 | 956,979 | 50.7% |