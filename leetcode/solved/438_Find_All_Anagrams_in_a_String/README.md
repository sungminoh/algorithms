### [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Medium

Given a string __s__ and a __non-empty__ string __p__, find all the start indices of __p__'s anagrams in __s__.

Strings consists of lowercase English letters only and the length of both strings __s__ and __p__ will not be larger than 20,100.

The order of output does not matter.

__Example 1:__

```
<b>Input:</b>
s: "cbaebabacd" p: "abc"

<b>Output:</b>
[0, 6]

<b>Explanation:</b>
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

__Example 2:__

```
<b>Input:</b>
s: "abab" p: "ab"

<b>Output:</b>
[0, 1, 2]

<b>Explanation:</b>
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 484,518 | 200,364 | 41.4% |