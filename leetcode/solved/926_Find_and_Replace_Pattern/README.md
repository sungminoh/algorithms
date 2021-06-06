### [926. Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)

Medium

Given a list of strings `` words `` and a string `` pattern ``, return _a list of_ `` words[i] `` _that match_ `` pattern ``. You may return the answer in __any order__.

A word matches the pattern if there exists a permutation of letters `` p `` so that after replacing every letter `` x `` in the pattern with `` p(x) ``, we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

__Example 1:__

```
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
```

__Example 2:__

```
Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
```

 

__Constraints:__

*   `` 1 <= pattern.length <= 20 ``
*   `` 1 <= words.length <= 50 ``
*   `` words[i].length == pattern.length ``
*   `` pattern `` and `` words[i] `` are lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 109,128 | 82,436 | 75.5% |