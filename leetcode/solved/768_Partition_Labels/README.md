### [768. Partition Labels](https://leetcode.com/problems/partition-labels/)

Medium

A string `` S `` of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

__Example 1:__

```
<b>Input:</b> S = "ababcbacadefegdehijhklij"
<b>Output:</b> [9,7,8]
<b>Explanation:</b>
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

 

__Note:__

*   `` S `` will have length in range `` [1, 500] ``.
*   `` S `` will consist of lowercase English letters (`` 'a' `` to `` 'z' ``) only.

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 223,061 | 172,210 | 77.2% |