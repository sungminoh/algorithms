### [1129. Longest String Chain](https://leetcode.com/problems/longest-string-chain/)

Medium

You are given an array of `` words `` where each word consists of lowercase English letters.

<code>word<sub>A</sub></code> is a __predecessor__ of <code>word<sub>B</sub></code> if and only if we can insert __exactly one__ letter anywhere in <code>word<sub>A</sub></code> __without changing the order of the other characters__ to make it equal to <code>word<sub>B</sub></code>.

*   For example, `` "abc" `` is a __predecessor__ of <code>"ab<u>a</u>c"</code>, while `` "cba" `` is not a __predecessor__ of `` "bcad" ``.

A __word chain___ _is a sequence of words <code>[word<sub>1</sub>, word<sub>2</sub>, ..., word<sub>k</sub>]</code> with `` k >= 1 ``, where <code>word<sub>1</sub></code> is a __predecessor__ of <code>word<sub>2</sub></code>, <code>word<sub>2</sub></code> is a __predecessor__ of <code>word<sub>3</sub></code>, and so on. A single word is trivially a __word chain__ with `` k == 1 ``.

Return _the __length__ of the __longest possible word chain__ with words chosen from the given list of _`` words ``.

 

__Example 1:__

```
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"].
```

__Example 2:__

```
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xb<u>c</u>", "<u>c</u>xbc", "<u>p</u>cxbc", "pcxbc<u>f</u>"].
```

__Example 3:__

```
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
```

 

__Constraints:__

*   `` 1 <= words.length <= 1000 ``
*   `` 1 <= words[i].length <= 16 ``
*   `` words[i] `` only consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 214,080 | 120,036 | 56.1% |