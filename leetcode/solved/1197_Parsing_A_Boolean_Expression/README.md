### [1197. Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/description/)

Hard

A __boolean expression__ is an expression that evaluates to either `` true `` or `` false ``. It can be in one of the following shapes:

*   `` 't' `` that evaluates to `` true ``.
*   `` 'f' `` that evaluates to `` false ``.
*   `` '!(subExpr)' `` that evaluates to __the logical NOT__ of the inner expression `` subExpr ``.
*   <code>'&(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)'</code> that evaluates to __the logical AND__ of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where `` n >= 1 ``.
*   <code>'|(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)'</code> that evaluates to __the logical OR__ of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where `` n >= 1 ``.

Given a string `` expression `` that represents a __boolean expression__, return _the evaluation of that expression_.

It is __guaranteed__ that the given expression is valid and follows the given rules.

 

<strong class="example">Example 1:</strong>

```
Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
```

<strong class="example">Example 2:</strong>

```
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
```

<strong class="example">Example 3:</strong>

```
Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
```

 

__Constraints:__

*   <code>1 <= expression.length <= 2 * 10<sup>4</sup></code>
*   expression\[i\] is one following characters: `` '(' ``, `` ')' ``, `` '&' ``, `` '|' ``, `` '!' ``, `` 't' ``, `` 'f' ``, and `` ',' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 49,955 | 29,516 | 59.1% |