### [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

Medium

Evaluate the value of an arithmetic expression in <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.

Valid operators are `` + ``, `` - ``, `` * ``, and `` / ``. Each operand may be an integer or another expression.

__Note__ that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

__Example 1:__

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

__Example 2:__

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

__Example 3:__

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
| 772,839 | 305,493 | 39.5% |