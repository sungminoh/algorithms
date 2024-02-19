### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/?envType=daily-question&envId=2024-02-06)

Medium

Given an array of strings `` strs ``, group __the anagrams__ together. You can return the answer in __any order__.

An __Anagram__ is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

<strong class="example">Example 1:</strong>

```Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

<strong class="example">Example 2:</strong>

```Input: strs = [""]
Output: [[""]]
```

<strong class="example">Example 3:</strong>

```Input: strs = ["a"]
Output: [["a"]]
```

 

__Constraints:__

*   <code>1 <= strs.length <= 10<sup>4</sup></code>
*   `` 0 <= strs[i].length <= 100 ``
*   `` strs[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 3,911,867 | 2,667,265 | 68.2% |