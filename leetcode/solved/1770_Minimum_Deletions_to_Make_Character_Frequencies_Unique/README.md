### [1770. Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)

Medium

A string `` s `` is called __good__ if there are no two different characters in `` s `` that have the same __frequency__.

Given a string `` s ``, return_ the __minimum__ number of characters you need to delete to make _`` s ``_ __good__._

The __frequency__ of a character in a string is the number of times it appears in the string. For example, in the string `` "aab" ``, the __frequency__ of `` 'a' `` is `` 2 ``, while the __frequency__ of `` 'b' `` is `` 1 ``.

 

__Example 1:__

<strong>Input:</strong> s = "aab"
    <strong>Output:</strong> 0
    <strong>Explanation:</strong> s is already good.

__Example 2:__

```
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
```

__Example 3:__

```
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` contains only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 253,470 | 150,509 | 59.4% |