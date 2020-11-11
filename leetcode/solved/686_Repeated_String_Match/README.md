### [686. Repeated String Match](https://leetcode.com/problems/repeated-string-match/)

Medium

Given two strings `` a `` and `` b ``, return the minimum number of times you should repeat the string `` a `` so that string `` b `` is a substring of it. If it's impossible for `` b ``​​​​​​ to be a substring of `` a `` after repeating it, return `` -1 ``.

__Notice:__ string `` "abc" `` repeated 0 times is `` "" ``,  repeated 1 time is `` "abc" `` and repeated 2 times is `` "abcabc" ``.

 

__Example 1:__

```
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
```

__Example 2:__

```
Input: a = "a", b = "aa"
Output: 2
```

__Example 3:__

```
Input: a = "a", b = "a"
Output: 1
```

__Example 4:__

```
Input: a = "abc, b = "wxyz"
Output: -1
```

 

__Constraints:__

*   <code>1 <= a.length <= 10<sup>4</sup></code>
*   <code>1 <= b.length <= 10<sup>4</sup></code>
*   `` a `` and `` b `` consist of lower-case English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 294,098 | 95,220 | 32.4% |