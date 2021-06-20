### [318. Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/)

Medium

Given a string array `` words ``, return _the maximum value of_ `` length(word[i]) * length(word[j]) `` _where the two words do not share common letters_. If no such two words exist, return `` 0 ``.

 

__Example 1:__

```
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
```

__Example 2:__

```
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
```

__Example 3:__

```
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
```

 

__Constraints:__

*   `` 2 <= words.length <= 1000 ``
*   `` 1 <= words[i].length <= 1000 ``
*   `` words[i] `` consists only of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 231,941 | 128,204 | 55.3% |