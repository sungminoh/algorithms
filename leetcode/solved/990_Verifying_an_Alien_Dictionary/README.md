### [990. Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)

Easy

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different `` order ``. The `` order `` of the alphabet is some permutation of lowercase letters.

Given a sequence of `` words `` written in the alien language, and the `` order `` of the alphabet, return `` true `` if and only if the given `` words `` are sorted lexicographicaly in this alien language.

 

__Example 1:__

```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

__Example 2:__

```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```

__Example 3:__

```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographical_order" target="_blank">More info</a>).
```

 

__Constraints:__

*   `` 1 <= words.length <= 100 ``
*   `` 1 <= words[i].length <= 20 ``
*   `` order.length == 26 ``
*   All characters in `` words[i] `` and `` order `` are English lowercase letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 441,918 | 231,810 | 52.5% |