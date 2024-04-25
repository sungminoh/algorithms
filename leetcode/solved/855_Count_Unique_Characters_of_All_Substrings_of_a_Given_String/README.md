### [855. Count Unique Characters of All Substrings of a Given String](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/)

Hard

Let's define a function `` countUniqueChars(s) `` that returns the number of unique characters in `` s ``.

*   For example, calling `` countUniqueChars(s) `` if `` s = "LEETCODE" `` then `` "L" ``, `` "T" ``, `` "C" ``, `` "O" ``, `` "D" `` are the unique characters since they appear only once in `` s ``, therefore `` countUniqueChars(s) = 5 ``.

Given a string `` s ``, return the sum of `` countUniqueChars(t) `` where `` t `` is a substring of `` s ``. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

 

<strong class="example">Example 1:</strong>

```
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
```

<strong class="example">Example 2:</strong>

<strong>Input:</strong> s = "ABA"
    <strong>Output:</strong> 8
    <strong>Explanation: </strong>The same as example 1, except countUniqueChars("ABA") = 1.

<strong class="example">Example 3:</strong>

```
Input: s = "LEETCODE"
Output: 92
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists of uppercase English letters only.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 135,690 | 70,947 | 52.3% |