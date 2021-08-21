### [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

Hard

A __transformation sequence__ from word `` beginWord `` to word `` endWord `` using a dictionary `` wordList `` is a sequence of words <code>beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub></code> such that:

*   Every adjacent pair of words differs by a single letter.
*   Every <code>s<sub>i</sub></code> for `` 1 <= i <= k `` is in `` wordList ``. Note that `` beginWord `` does not need to be in `` wordList ``.
*   <code>s<sub>k</sub> == endWord</code>

Given two words, `` beginWord `` and `` endWord ``, and a dictionary `` wordList ``, return _all the __shortest transformation sequences__ from_ `` beginWord `` _to_ `` endWord ``_, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words _<code>[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]</code>.

 

__Example 1:__

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```

__Example 2:__

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

 

__Constraints:__

*   `` 1 <= beginWord.length <= 5 ``
*   `` endWord.length == beginWord.length ``
*   `` 1 <= wordList.length <= 1000 ``
*   `` wordList[i].length == beginWord.length ``
*   `` beginWord ``, `` endWord ``, and `` wordList[i] `` consist of lowercase English letters.
*   `` beginWord != endWord ``
*   All the words in `` wordList `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,000,871 | 253,246 | 25.3% |