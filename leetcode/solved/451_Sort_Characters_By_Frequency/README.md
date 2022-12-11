### [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

Medium

Given a string `` s ``, sort it in __decreasing order__ based on the __frequency__ of the characters. The __frequency__ of a character is the number of times it appears in the string.

Return _the sorted string_. If there are multiple answers, return _any of them_.

 

<strong class="example">Example 1:</strong>

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

<strong class="example">Example 2:</strong>

```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
```

<strong class="example">Example 3:</strong>

```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

 

__Constraints:__

*   <code>1 <= s.length <= 5 * 10<sup>5</sup></code>
*   `` s `` consists of uppercase and lowercase English letters and digits.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 674,231 | 470,992 | 69.9% |