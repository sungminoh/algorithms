### [1756. Minimum Deletions to Make String Balanced](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2024-07-30)

Medium

You are given a string `` s `` consisting only of characters `` 'a' `` and `` 'b' ``​​​​.

You can delete any number of characters in `` s `` to make `` s `` __balanced__. `` s `` is __balanced__ if there is no pair of indices `` (i,j) `` such that `` i < j `` and `` s[i] = 'b' `` and `` s[j]= 'a' ``.

Return _the __minimum__ number of deletions needed to make _`` s ``_ __balanced___.

 

<strong class="example">Example 1:</strong>

```
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aa<u>b</u>abb<u>a</u>b" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aab<u>a</u>bb<u>a</u>b" -> "aabbbb").
```

<strong class="example">Example 2:</strong>

```
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s[i] `` is `` 'a' `` or `` 'b' ``​​.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 250,726 | 164,886 | 65.8% |