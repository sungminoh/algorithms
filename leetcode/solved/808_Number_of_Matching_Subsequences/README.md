### [808. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)

Medium

Given a string `` s `` and an array of strings `` words ``, return _the number of_ `` words[i] `` _that is a subsequence of_ `` s ``.

A __subsequence__ of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

*   For example, `` "ace" `` is a subsequence of `` "abcde" ``.

 

__Example 1:__

```
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
```

__Example 2:__

```
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
```

 

__Constraints:__

*   <code>1 <= s.length <= 5 * 10<sup>4</sup></code>
*   `` 1 <= words.length <= 5000 ``
*   `` 1 <= words[i].length <= 50 ``
*   `` s `` and `` words[i] `` consist of only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 185,256 | 90,935 | 49.1% |