### [1251. Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/)

Hard

You are given a string `` text ``. You should split it to k substrings <code>(subtext<sub>1</sub>, subtext<sub>2</sub>, ..., subtext<sub>k</sub>)</code> such that:

*   <code>subtext<sub>i</sub></code> is a __non-empty__ string.
*   The concatenation of all the substrings is equal to `` text `` (i.e., <code>subtext<sub>1</sub> + subtext<sub>2</sub> + ... + subtext<sub>k</sub> == text</code>).
*   <code>subtext<sub>i</sub> == subtext<sub>k - i + 1</sub></code> for all valid values of `` i `` (i.e., `` 1 <= i <= k ``).

Return the largest possible value of `` k ``.

 

<strong class="example">Example 1:</strong>

```
Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
```

<strong class="example">Example 2:</strong>

```
Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
```

<strong class="example">Example 3:</strong>

```
Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".
```

 

__Constraints:__

*   `` 1 <= text.length <= 1000 ``
*   `` text `` consists only of lowercase English characters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 40,144 | 23,570 | 58.7% |