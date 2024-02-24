### [2059. Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2023-11-14)

Medium

Given a string `` s ``, return _the number of __unique palindromes of length three__ that are a __subsequence__ of _`` s ``.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted __once__.

A __palindrome__ is a string that reads the same forwards and backwards.

A __subsequence__ of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

*   For example, `` "ace" `` is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code>.

 

<strong class="example">Example 1:</strong>

```
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "<u>a</u>a<u>b</u>c<u>a</u>")
- "aaa" (subsequence of "<u>aa</u>bc<u>a</u>")
- "aca" (subsequence of "<u>a</u>ab<u>ca</u>")
```

<strong class="example">Example 2:</strong>

```
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
```

<strong class="example">Example 3:</strong>

```
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "<u>bb</u>c<u>b</u>aba")
- "bcb" (subsequence of "<u>b</u>b<u>cb</u>aba")
- "bab" (subsequence of "<u>b</u>bcb<u>ab</u>a")
- "aba" (subsequence of "bbcb<u>aba</u>")
```

 

__Constraints:__

*   <code>3 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists of only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 151,601 | 100,216 | 66.1% |