### [139. Word Break](https://leetcode.com/problems/word-break/)

Medium

Given a string `` s `` and a dictionary of strings `` wordDict ``, return `` true `` if `` s `` can be segmented into a space-separated sequence of one or more dictionary words.

__Note__ that the same word in the dictionary may be reused multiple times in the segmentation.

 

<strong class="example">Example 1:</strong>

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

<strong class="example">Example 2:</strong>

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

<strong class="example">Example 3:</strong>

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

 

__Constraints:__

*   `` 1 <= s.length <= 300 ``
*   `` 1 <= wordDict.length <= 1000 ``
*   `` 1 <= wordDict[i].length <= 20 ``
*   `` s `` and `` wordDict[i] `` consist of only lowercase English letters.
*   All the strings of `` wordDict `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,848,499 | 1,297,440 | 45.5% |