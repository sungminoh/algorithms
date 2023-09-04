### [1894. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/?envType=daily-question&envId=2023-04-18)

Easy

You are given two strings `` word1 `` and `` word2 ``. Merge the strings by adding letters in alternating order, starting with `` word1 ``. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return _the merged string._

 

<strong class="example">Example 1:</strong>

```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

<strong class="example">Example 2:</strong>

```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
```

<strong class="example">Example 3:</strong>

```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

 

__Constraints:__

*   `` 1 <= word1.length, word2.length <= 100 ``
*   `` word1 `` and `` word2 `` consist of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 465,380 | 370,831 | 79.7% |