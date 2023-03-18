### [1146. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

Easy

For two strings `` s `` and `` t ``, we say "`` t `` divides `` s ``" if and only if `` s = t + ... + t `` (i.e., `` t `` is concatenated with itself one or more times).

Given two strings `` str1 `` and `` str2 ``, return _the largest string _`` x ``_ such that _`` x ``_ divides both _`` str1 ``_ and _`` str2 ``.

 

<strong class="example">Example 1:</strong>

```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

<strong class="example">Example 2:</strong>

```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

<strong class="example">Example 3:</strong>

```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

 

__Constraints:__

*   `` 1 <= str1.length, str2.length <= 1000 ``
*   `` str1 `` and `` str2 `` consist of English uppercase letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 285,261 | 161,519 | 56.6% |