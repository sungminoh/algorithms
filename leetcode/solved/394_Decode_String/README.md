### [394. Decode String](https://leetcode.com/problems/decode-string/)

Medium

Given an encoded string, return its decoded string.

The encoding rule is: `` k[encoded_string] ``, where the `` encoded_string `` inside the square brackets is being repeated exactly `` k `` times. Note that `` k `` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `` k ``. For example, there will not be input like `` 3a `` or `` 2[4] ``.

 

__Example 1:__

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

__Example 2:__

```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

__Example 3:__

```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

 

__Constraints:__

*   `` 1 <= s.length <= 30 ``
*   `` s `` consists of lowercase English letters, digits, and square brackets `` '[]' ``.
*   `` s `` is guaranteed to be __a valid__ input.
*   All the integers in `` s `` are in the range `` [1, 300] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 775,085 | 430,528 | 55.5% |