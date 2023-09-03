### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/?envType=daily-question&envId=2023-04-10)

Easy

Given a string `` s `` containing just the characters `` '(' ``, `` ')' ``, `` '{' ``, `` '}' ``, `` '[' `` and `` ']' ``, determine if the input string is valid.

An input string is valid if:

1.   Open brackets must be closed by the same type of brackets.
2.   Open brackets must be closed in the correct order.
3.   Every close bracket has a corresponding open bracket of the same type.

 

<strong class="example">Example 1:</strong>

```
Input: s = "()"
Output: true
```

<strong class="example">Example 2:</strong>

```
Input: s = "()[]{}"
Output: true
```

<strong class="example">Example 3:</strong>

```
Input: s = "(]"
Output: false
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>4</sup></code>
*   `` s `` consists of parentheses only `` '()[]{}' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 9,220,453 | 3,706,709 | 40.2% |