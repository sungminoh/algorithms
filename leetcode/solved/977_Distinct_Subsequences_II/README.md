### [977. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/description/)

Hard

Given a string s, return _the number of __distinct non-empty subsequences__ of_ `` s ``. Since the answer may be very large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

A __subsequence__ of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `` "ace" `` is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code> while `` "aec" `` is not.
 

<strong class="example">Example 1:</strong>

```
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
```

<strong class="example">Example 2:</strong>

```
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
```

<strong class="example">Example 3:</strong>

```
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
```

 

__Constraints:__

*   `` 1 <= s.length <= 2000 ``
*   `` s `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 90,343 | 38,974 | 43.1% |