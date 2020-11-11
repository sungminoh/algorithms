### [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

Medium

Given a string `` s `` that consists of only uppercase English letters, you can perform at most `` k `` operations on that string.

In one operation, you can choose __any__ character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

__Note:__  
Both the string's length and _k_ will not exceed 10<sup>4</sup>.

__Example 1:__

```
<b>Input:</b>
s = "ABAB", k = 2

<b>Output:</b>
4

<b>Explanation:</b>
Replace the two 'A's with two 'B's or vice versa.
```

 

__Example 2:__

```
<b>Input:</b>
s = "AABABBA", k = 1

<b>Output:</b>
4

<b>Explanation:</b>
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 125,895 | 57,619 | 45.8% |