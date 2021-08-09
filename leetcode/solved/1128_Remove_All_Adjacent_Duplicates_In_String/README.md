### [1128. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

Easy

You are given a string `` s `` consisting of lowercase English letters. A __duplicate removal__ consists of choosing two __adjacent__ and __equal__ letters and removing them.

We repeatedly make __duplicate removals__ on `` s `` until we no longer can.

Return _the final string after all such duplicate removals have been made_. It can be proven that the answer is __unique__.

 

__Example 1:__

```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

__Example 2:__

```
Input: s = "azxxzy"
Output: "ay"
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 269,122 | 192,324 | 71.5% |