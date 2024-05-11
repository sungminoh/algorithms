### [957. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)

Medium

A parentheses string is valid if and only if:

*   It is the empty string,
*   It can be written as `` AB `` (`` A `` concatenated with `` B ``), where `` A `` and `` B `` are valid strings, or
*   It can be written as `` (A) ``, where `` A `` is a valid string.

You are given a parentheses string `` s ``. In one move, you can insert a parenthesis at any position of the string.

*   For example, if `` s = "()))" ``, you can insert an opening parenthesis to be <code>"(<strong>(</strong>)))"</code> or a closing parenthesis to be <code>"())<strong>)</strong>)"</code>.

Return _the minimum number of moves required to make _`` s ``_ valid_.

 

<strong class="example">Example 1:</strong>

```
Input: s = "())"
Output: 1
```

<strong class="example">Example 2:</strong>

```
Input: s = "((("
Output: 3
```

 

__Constraints:__

*   `` 1 <= s.length <= 1000 ``
*   `` s[i] `` is either `` '(' `` or `` ')' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 454,311 | 341,388 | 75.1% |