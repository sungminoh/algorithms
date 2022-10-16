### [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

Hard

You are given a __0-indexed__ array of __unique__ strings `` words ``.

A __palindrome pair__ is a pair of integers `` (i, j) `` such that:

*   `` 0 <= i, j < word.length ``,
*   `` i != j ``, and
*   `` words[i] + words[j] `` (the concatenation of the two strings) is a palindrome string.

Return _an array of all the __palindrome pairs__ of _`` words ``.

 

<strong class="example">Example 1:</strong>

```
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
```

<strong class="example">Example 2:</strong>

```
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
```

<strong class="example">Example 3:</strong>

```
Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]
```

 

__Constraints:__

*   `` 1 <= words.length <= 5000 ``
*   `` 0 <= words[i].length <= 300 ``
*   `` words[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 525,418 | 185,085 | 35.2% |