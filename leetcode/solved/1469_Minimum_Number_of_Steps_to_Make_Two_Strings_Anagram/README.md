### [1469. Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-13)

Medium

You are given two strings of the same length `` s `` and `` t ``. In one step you can choose __any character__ of `` t `` and replace it with __another character__.

Return _the minimum number of steps_ to make `` t `` an anagram of `` s ``.

An __Anagram__ of a string is a string that contains the same characters with a different (or the same) ordering.

 

<strong class="example">Example 1:</strong>

```
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
```

<strong class="example">Example 2:</strong>

```
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
```

<strong class="example">Example 3:</strong>

```
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
```

 

__Constraints:__

*   <code>1 <= s.length <= 5 * 10<sup>4</sup></code>
*   `` s.length == t.length ``
*   `` s `` and `` t `` consist of lowercase English letters only.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 318,120 | 260,707 | 82.0% |