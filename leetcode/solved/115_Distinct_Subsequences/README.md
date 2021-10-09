### [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

Hard

Given two strings `` s `` and `` t ``, return _the number of distinct subsequences of `` s `` which equals `` t ``_.

A string's __subsequence__ is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., `` "ACE" `` is a subsequence of `` "ABCDE" `` while `` "AEC" `` is not).

It is guaranteed the answer fits on a 32-bit signed integer.

 

__Example 1:__

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
<code><u>rabb</u>b<u>it</u></code>
<code><u>ra</u>b<u>bbit</u></code>
<code><u>rab</u>b<u>bit</u></code>
```

__Example 2:__

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
<code><u>ba</u>b<u>g</u>bag</code>
<code><u>ba</u>bgba<u>g</u></code>
<code><u>b</u>abgb<u>ag</u></code>
<code>ba<u>b</u>gb<u>ag</u></code>
<code>babg<u>bag</u></code>
```

 

__Constraints:__

*   `` 1 <= s.length, t.length <= 1000 ``
*   `` s `` and `` t `` consist of English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 471,433 | 195,756 | 41.5% |