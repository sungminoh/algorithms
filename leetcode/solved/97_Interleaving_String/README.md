### [97. Interleaving String](https://leetcode.com/problems/interleaving-string/)

Medium

Given strings `` s1 ``, `` s2 ``, and `` s3 ``, find whether `` s3 `` is formed by an __interleaving__ of `` s1 `` and `` s2 ``.

An __interleaving__ of two strings `` s `` and `` t `` is a configuration where they are divided into __non-empty__ substrings such that:

*   <code>s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub></code>
*   <code>t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub></code>
*   `` |n - m| <= 1 ``
*   The __interleaving__ is <code>s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...</code> or <code>t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...</code>

__Note:__ `` a + b `` is the concatenation of strings `` a `` and `` b ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg" style="width: 561px; height: 203px;"/>

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
```

__Example 2:__

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

__Example 3:__

```
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

 

__Constraints:__

*   `` 0 <= s1.length, s2.length <= 100 ``
*   `` 0 <= s3.length <= 200 ``
*   `` s1 ``, `` s2 ``, and `` s3 `` consist of lowercase English letters.

 

__Follow up:__ Could you solve it using only `` O(s2.length) `` additional memory space?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 631,549 | 212,485 | 33.6% |