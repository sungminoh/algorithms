### [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/)

Hard

Given a list of words (__without duplicates__), please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

__Example:__  

```
<b>Input:</b> ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

<b>Output:</b> ["catsdogcats","dogcatsdog","ratcatdogcat"]

<b>Explanation:</b> "catsdogcats" can be concatenated by "cats", "dog" and "cats"; <br/> "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; <br/>"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

__Note:__  

1.   The number of elements of the given array will not exceed `` 10,000  ``<li>The length sum of elements in the given array will not exceed <code>600,000</code>. </li><li>All the input string will only include lower case letters.</li><li>The returned elements order does not matter. </li>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 169,170 | 75,583 | 44.7% |