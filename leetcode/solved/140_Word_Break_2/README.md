### [140. Word Break II](https://leetcode.com/problems/word-break-ii/description/)

[Description](https://leetcode.com/problems/word-break-ii/description/)[Hints](https://leetcode.com/problems/word-break-ii/hints/)[Submissions](https://leetcode.com/problems/word-break-ii/submissions/)[Discuss](https://leetcode.com/problems/word-break-ii/discuss/)[Solution](https://leetcode.com/problems/word-break-ii/solution/)



[Pick One](https://leetcode.com/problems/random-one-question/)

------

Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, add spaces in *s* to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

**Note:**

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

**Example 1:**

```
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```

**Example 2:**

```
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
```