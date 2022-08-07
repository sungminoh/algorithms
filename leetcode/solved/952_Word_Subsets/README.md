### [952. Word Subsets](https://leetcode.com/problems/word-subsets/)

Medium

You are given two string arrays `` words1 `` and `` words2 ``.

A string `` b `` is a __subset__ of string `` a `` if every letter in `` b `` occurs in `` a `` including multiplicity.

*   For example, `` "wrr" `` is a subset of `` "warrior" `` but is not a subset of `` "world" ``.

A string `` a `` from `` words1 `` is __universal__ if for every string `` b `` in `` words2 ``, `` b `` is a subset of `` a ``.

Return an array of all the __universal__ strings in `` words1 ``. You may return the answer in __any order__.

 

__Example 1:__

```
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
```

__Example 2:__

```
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
```

 

__Constraints:__

*   <code>1 <= words1.length, words2.length <= 10<sup>4</sup></code>
*   `` 1 <= words1[i].length, words2[i].length <= 10 ``
*   `` words1[i] `` and `` words2[i] `` consist only of lowercase English letters.
*   All the strings of `` words1 `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 184,796 | 100,251 | 54.2% |