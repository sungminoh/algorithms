### [1170. Shortest Common Supersequence ](https://leetcode.com/problems/shortest-common-supersequence/description/)

Hard

Given two strings `` str1 `` and `` str2 ``, return _the shortest string that has both _`` str1 ``_ and _`` str2 ``_ as __subsequences___. If there are multiple valid strings, return __any__ of them.

A string `` s `` is a __subsequence__ of string `` t `` if deleting some number of characters from `` t `` (possibly `` 0 ``) results in the string `` s ``.

 

<strong class="example">Example 1:</strong>

```
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
```

<strong class="example">Example 2:</strong>

```
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
```

 

__Constraints:__

*   `` 1 <= str1.length, str2.length <= 1000 ``
*   `` str1 `` and `` str2 `` consist of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 187,471 | 110,603 | 59.0% |