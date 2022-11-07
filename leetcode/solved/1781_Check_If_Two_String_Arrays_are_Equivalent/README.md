### [1781. Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)

Easy

Given two string arrays `` word1 `` and `` word2 ``, return_ _`` true ``_ if the two arrays __represent__ the same string, and _`` false ``_ otherwise._

A string is __represented__ by an array if the array elements concatenated __in order__ forms the string.

 

<strong class="example">Example 1:</strong>

```
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
```

<strong class="example">Example 2:</strong>

```
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
```

<strong class="example">Example 3:</strong>

```
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
```

 

__Constraints:__

*   <code>1 <= word1.length, word2.length <= 10<sup>3</sup></code>
*   <code>1 <= word1[i].length, word2[i].length <= 10<sup>3</sup></code>
*   <code>1 <= sum(word1[i].length), sum(word2[i].length) <= 10<sup>3</sup></code>
*   `` word1[i] `` and `` word2[i] `` consist of lowercase letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 293,691 | 244,493 | 83.2% |