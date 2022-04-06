### [768. Partition Labels](https://leetcode.com/problems/partition-labels/)

Medium

You are given a string `` s ``. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `` s ``.

Return _a list of integers representing the size of these parts_.

 

__Example 1:__

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

__Example 2:__

```
Input: s = "eccbbbbdec"
Output: [10]
```

 

__Constraints:__

*   `` 1 <= s.length <= 500 ``
*   `` s `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 473,118 | 376,247 | 79.5% |