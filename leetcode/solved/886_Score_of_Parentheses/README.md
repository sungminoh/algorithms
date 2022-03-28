### [886. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

Medium

Given a balanced parentheses string `` s ``, return _the __score__ of the string_.

The __score__ of a balanced parentheses string is based on the following rule:

*   `` "()" `` has score `` 1 ``.
*   `` AB `` has score `` A + B ``, where `` A `` and `` B `` are balanced parentheses strings.
*   `` (A) `` has score `` 2 * A ``, where `` A `` is a balanced parentheses string.

 

__Example 1:__

```
Input: s = "()"
Output: 1
```

__Example 2:__

```
Input: s = "(())"
Output: 2
```

__Example 3:__

```
Input: s = "()()"
Output: 2
```

 

__Constraints:__

*   `` 2 <= s.length <= 50 ``
*   `` s `` consists of only `` '(' `` and `` ')' ``.
*   `` s `` is a balanced parentheses string.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 204,362 | 133,792 | 65.5% |