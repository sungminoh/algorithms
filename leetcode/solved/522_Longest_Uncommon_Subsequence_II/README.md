### [522. Longest Uncommon Subsequence II](https://leetcode.com/problems/longest-uncommon-subsequence-ii/)

Medium

Given an array of strings `` strs ``, return _the length of the __longest uncommon subsequence__ between them_. If the longest uncommon subsequence does not exist, return `` -1 ``.

An __uncommon subsequence__ between an array of strings is a string that is a __subsequence of one string but not the others__.

A __subsequence__ of a string `` s `` is a string that can be obtained after deleting any number of characters from `` s ``.

*   For example, `` "abc" `` is a subsequence of `` "aebdc" `` because you can delete the underlined characters in <code>"a<u>e</u>b<u>d</u>c"</code> to get `` "abc" ``. Other subsequences of `` "aebdc" `` include `` "aebdc" ``, `` "aeb" ``, and `` "" `` (empty string).

 

__Example 1:__

```Input: strs = ["aba","cdc","eae"]
Output: 3
```

__Example 2:__

```Input: strs = ["aaa","aaa","aa"]
Output: -1
```

 

__Constraints:__

*   `` 2 <= strs.length <= 50 ``
*   `` 1 <= strs[i].length <= 10 ``
*   `` strs[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 100,395 | 39,890 | 39.7% |