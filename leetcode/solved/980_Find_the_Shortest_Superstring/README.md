### [980. Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/)

Hard

Given an array of strings `` words ``, return _the smallest string that contains each string in_ `` words `` _as a substring_. If there are multiple valid strings of the smallest length, return __any of them__.

You may assume that no string in `` words `` is a substring of another string in `` words ``.

 

__Example 1:__

```
Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
```

__Example 2:__

```
Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
```

 

__Constraints:__

*   `` 1 <= words.length <= 12 ``
*   `` 1 <= words[i].length <= 20 ``
*   `` words[i] `` consists of lowercase English letters.
*   All the strings of `` words `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 45,179 | 20,761 | 46.0% |