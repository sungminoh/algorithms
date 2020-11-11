### [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

Hard

Given a list of __unique__ words, return all the pairs of the ___distinct___ indices `` (i, j) `` in the given list, so that the concatenation of the two words `` words[i] + words[j] `` is a palindrome.

 

__Example 1:__

```
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
```

__Example 2:__

```
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
```

__Example 3:__

```
Input: words = ["a",""]
Output: [[0,1],[1,0]]
```

 

__Constraints:__

*   `` 1 <= words.length <= 5000 ``
*   `` 0 <= words[i] <= 300 ``
*   `` words[i] `` consists of lower-case English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 307,254 | 104,470 | 34.0% |