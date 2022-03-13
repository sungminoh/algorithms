### [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

Easy

Given two strings `` s `` and `` t ``, return `` true ``_ if _`` s ``_ is a __subsequence__ of _`` t ``_, or _`` false ``_ otherwise_.

A __subsequence__ of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `` "ace" `` is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code> while `` "aec" `` is not).

 

__Example 1:__

```Input: s = "abc", t = "ahbgdc"
Output: true
```

__Example 2:__

```Input: s = "axc", t = "ahbgdc"
Output: false
```

 

__Constraints:__

*   `` 0 <= s.length <= 100 ``
*   <code>0 <= t.length <= 10<sup>4</sup></code>
*   `` s `` and `` t `` consist only of lowercase English letters.

 
__Follow up:__ Suppose there are lots of incoming `` s ``, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k >= 10<sup>9</sup></code>, and you want to check one by one to see if `` t `` has its subsequence. In this scenario, how would you change your code?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 867,858 | 442,081 | 50.9% |