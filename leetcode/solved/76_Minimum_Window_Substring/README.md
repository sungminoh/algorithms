### [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/?envType=daily-question&envId=2024-02-04)

Hard

Given two strings `` s `` and `` t `` of lengths `` m `` and `` n `` respectively, return _the __minimum window___ <span data-keyword="substring-nonempty">___substring___</span>_ of _`` s ``_ such that every character in _`` t ``_ (__including duplicates__) is included in the window_. If there is no such substring, return _the empty string _`` "" ``.

The testcases will be generated such that the answer is __unique__.

 

<strong class="example">Example 1:</strong>

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

<strong class="example">Example 2:</strong>

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

<strong class="example">Example 3:</strong>

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

 

__Constraints:__

*   `` m == s.length ``
*   `` n == t.length ``
*   <code>1 <= m, n <= 10<sup>5</sup></code>
*   `` s `` and `` t `` consist of uppercase and lowercase English letters.

 

__Follow up:__ Could you find an algorithm that runs in `` O(m + n) `` time?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,995,438 | 1,279,017 | 42.7% |