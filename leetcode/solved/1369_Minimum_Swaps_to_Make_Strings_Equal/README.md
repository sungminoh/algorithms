### [1369. Minimum Swaps to Make Strings Equal](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/)

Medium

You are given two strings `` s1 `` and `` s2 `` of equal length consisting of letters `` "x" `` and `` "y" `` __only__. Your task is to make these two strings equal to each other. You can swap any two characters that belong to __different__ strings, which means: swap `` s1[i] `` and `` s2[j] ``.

Return the minimum number of swaps required to make `` s1 `` and `` s2 `` equal, or return `` -1 `` if it is impossible to do so.

 

<strong class="example">Example 1:</strong>

```
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
```

<strong class="example">Example 2:</strong>

```
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
```

<strong class="example">Example 3:</strong>

```
Input: s1 = "xx", s2 = "xy"
Output: -1
```

 

__Constraints:__

*   `` 1 <= s1.length, s2.length <= 1000 ``
*   `` s1.length == s2.length ``
*   `` s1, s2 `` only contain `` 'x' `` or `` 'y' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 60,962 | 39,296 | 64.5% |