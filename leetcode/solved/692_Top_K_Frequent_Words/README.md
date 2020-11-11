### [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

Medium

Given a non-empty list of words, return the _k_ most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

__Example 1:__  

```
<b>Input:</b> ["i", "love", "leetcode", "i", "love", "coding"], k = 2
<b>Output:</b> ["i", "love"]
<b>Explanation:</b> "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

__Example 2:__  

```
<b>Input:</b> ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
<b>Output:</b> ["the", "is", "sunny", "day"]
<b>Explanation:</b> "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

__Note:__  

1.   You may assume _k_ is always valid, 1 ≤ _k_ ≤ number of unique elements.
2.   Input words contain only lowercase letters.

__Follow up:__  

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 374,297 | 194,685 | 52.0% |