### [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/)

Hard

Given an array of strings `` words `` (__without duplicates__), return _all the __concatenated words__ in the given list of_ `` words ``.

A __concatenated word__ is defined as a string that is comprised entirely of at least two shorter words (not necesssarily distinct) in the given array.

 

<strong class="example">Example 1:</strong>

```
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

<strong class="example">Example 2:</strong>

```
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
```

 

__Constraints:__

*   <code>1 <= words.length <= 10<sup>4</sup></code>
*   `` 1 <= words[i].length <= 30 ``
*   `` words[i] `` consists of only lowercase English letters.
*   All the strings of `` words `` are __unique__.
*   <code>1 <= sum(words[i].length) <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 411,205 | 205,969 | 50.1% |