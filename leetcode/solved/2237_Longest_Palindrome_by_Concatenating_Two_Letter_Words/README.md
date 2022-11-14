### [2237. Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)

Medium

You are given an array of strings `` words ``. Each element of `` words `` consists of __two__ lowercase English letters.

Create the __longest possible palindrome__ by selecting some elements from `` words `` and concatenating them in __any order__. Each element can be selected __at most once__.

Return _the __length__ of the longest palindrome that you can create_. If it is impossible to create any palindrome, return `` 0 ``.

A __palindrome__ is a string that reads the same forward and backward.

 

<strong class="example">Example 1:</strong>

```
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
```

<strong class="example">Example 2:</strong>

```
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
```

<strong class="example">Example 3:</strong>

```
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
```

 

__Constraints:__

*   <code>1 <= words.length <= 10<sup>5</sup></code>
*   `` words[i].length == 2 ``
*   `` words[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 175,658 | 86,448 | 49.2% |