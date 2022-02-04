### [290. Word Pattern](https://leetcode.com/problems/word-pattern/)

Easy

Given a `` pattern `` and a string `` s ``, find if `` s `` follows the same pattern.

Here __follow__ means a full match, such that there is a bijection between a letter in `` pattern `` and a __non-empty__ word in `` s ``.

 

__Example 1:__

```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

__Example 2:__

```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

__Example 3:__

```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

 

__Constraints:__

*   `` 1 <= pattern.length <= 300 ``
*   `` pattern `` contains only lower-case English letters.
*   `` 1 <= s.length <= 3000 ``
*   `` s `` contains only lowercase English letters and spaces `` ' ' ``.
*   `` s `` __does not contain__ any leading or trailing spaces.
*   All the words in `` s `` are separated by a __single space__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 844,565 | 338,270 | 40.1% |