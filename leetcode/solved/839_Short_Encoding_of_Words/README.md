### [839. Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/)

Medium

A __valid encoding__ of an array of `` words `` is any reference string `` s `` and array of indices `` indices `` such that:

*   `` words.length == indices.length ``
*   The reference string `` s `` ends with the `` '#' `` character.
*   For each index `` indices[i] ``, the __substring__ of `` s `` starting from `` indices[i] `` and up to (but not including) the next `` '#' `` character is equal to `` words[i] ``.

Given an array of `` words ``, return _the __length of the shortest reference string__ _`` s ``_ possible of any __valid encoding__ of _`` words ``_._

 

__Example 1:__

<strong>Input:</strong> words = ["time", "me", "bell"]
    <strong>Output:</strong> 10
    <strong>Explanation:</strong> A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
    words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "<u>time</u>#bell#"
    words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "ti<u>me</u>#bell#"
    words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#<u>bell</u>#"

__Example 2:__

```
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
```

 

__Constraints:__

*   `` 1 <= words.length <= 2000 ``
*   `` 1 <= words[i].length <= 7 ``
*   `` words[i] `` consists of only lowercase letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 142,602 | 86,505 | 60.7% |