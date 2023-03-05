### [140. Word Break II](https://leetcode.com/problems/word-break-ii/)

Hard

Given a string `` s `` and a dictionary of strings `` wordDict ``, add spaces in `` s `` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in __any order__.

__Note__ that the same word in the dictionary may be reused multiple times in the segmentation.

 

<strong class="example">Example 1:</strong>

```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

<strong class="example">Example 2:</strong>

```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
```

<strong class="example">Example 3:</strong>

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
```

 

__Constraints:__

*   `` 1 <= s.length <= 20 ``
*   `` 1 <= wordDict.length <= 1000 ``
*   `` 1 <= wordDict[i].length <= 10 ``
*   `` s `` and `` wordDict[i] `` consist of only lowercase English letters.
*   All the strings of `` wordDict `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,121,011 | 506,088 | 45.1% |