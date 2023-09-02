### [2487. Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/)

Medium

Given a string `` s ``, partition the string into one or more __substrings__ such that the characters in each substring are __unique__. That is, no letter appears in a single substring more than __once__.

Return _the __minimum__ number of substrings in such a partition._

Note that each character should belong to exactly one substring in a partition.

 

<strong class="example">Example 1:</strong>

```
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
```

<strong class="example">Example 2:</strong>

```
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists of only English lowercase letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 170,049 | 134,549 | 79.1% |