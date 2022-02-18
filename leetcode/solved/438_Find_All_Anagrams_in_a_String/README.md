### [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Medium

Given two strings `` s `` and `` p ``, return _an array of all the start indices of _`` p ``_'s anagrams in _`` s ``. You may return the answer in __any order__.

An __Anagram__ is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

__Example 1:__

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

__Example 2:__

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

 

__Constraints:__

*   <code>1 <= s.length, p.length <= 3 * 10<sup>4</sup></code>
*   `` s `` and `` p `` consist of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,031,734 | 493,890 | 47.9% |