### [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Easy

Given two strings `` needle `` and `` haystack ``, return the index of the first occurrence of `` needle `` in `` haystack ``, or `` -1 `` if `` needle `` is not part of `` haystack ``.

 

<strong class="example">Example 1:</strong>

```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

<strong class="example">Example 2:</strong>

```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

 

__Constraints:__

*   <code>1 <= haystack.length, needle.length <= 10<sup>4</sup></code>
*   `` haystack `` and `` needle `` consist of only lowercase English characters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 4,270,305 | 1,668,245 | 39.1% |