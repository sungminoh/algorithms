### [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

Hard

Given two strings `` s `` and `` t `` of lengths `` m `` and `` n `` respectively, return _the __minimum window substring__ of _`` s ``_ such that every character in _`` t ``_ (__including duplicates__) is included in the window. If there is no such substring__, return the empty string _`` "" ``_._

The testcases will be generated such that the answer is __unique__.

A __substring__ is a contiguous sequence of characters within the string.

 

__Example 1:__

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

__Example 2:__

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

__Example 3:__

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

 

__Constraints:__

*   `` m == s.length ``
*   `` n == t.length ``
*   <code>1 <= m, n <= 10<sup>5</sup></code>
*   `` s `` and `` t `` consist of uppercase and lowercase English letters.

 
__Follow up:__ Could you find an algorithm that runs in `` O(m + n) `` time?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,612,218 | 603,766 | 37.4% |