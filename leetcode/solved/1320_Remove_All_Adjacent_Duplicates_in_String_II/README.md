### [1320. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

Medium

You are given a string `` s `` and an integer `` k ``, a `` k `` __duplicate removal__ consists of choosing `` k `` adjacent and equal letters from `` s `` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `` k `` __duplicate removals__ on `` s `` until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

__Example 1:__

```
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
```

__Example 2:__

```
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa.
```

__Example 3:__

```
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   <code>2 <= k <= 10<sup>4</sup></code>
*   `` s `` only contains lower case English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 369,792 | 207,893 | 56.2% |