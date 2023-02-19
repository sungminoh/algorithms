### [1250. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

Medium

Given two strings `` text1 `` and `` text2 ``, return _the length of their longest __common subsequence__. _If there is no __common subsequence__, return `` 0 ``.

A __subsequence__ of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

*   For example, `` "ace" `` is a subsequence of `` "abcde" ``.

A __common subsequence__ of two strings is a subsequence that is common to both strings.

 

<strong class="example">Example 1:</strong>

```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

<strong class="example">Example 2:</strong>

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

<strong class="example">Example 3:</strong>

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

 

__Constraints:__

*   `` 1 <= text1.length, text2.length <= 1000 ``
*   `` text1 `` and `` text2 `` consist of only lowercase English characters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,112,126 | 650,446 | 58.5% |