### [522. Longest Uncommon Subsequence II](https://leetcode.com/problems/longest-uncommon-subsequence-ii/)

Medium

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be __any__ subsequence of the other strings.

A __subsequence__ is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

__Example 1:__  

```
<b>Input:</b> "aba", "cdc", "eae"
<b>Output:</b> 3
```

__Note:__

1.   All the given strings' lengths will not exceed 10.
2.   The length of the given list will be in the range of \[2, 50\].

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 62,590 | 21,114 | 33.7% |