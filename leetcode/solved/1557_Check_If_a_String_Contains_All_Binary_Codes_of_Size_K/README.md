### [1557. Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)

Medium

Given a binary string `` s `` and an integer `` k ``, return `` true `` _if every binary code of length_ `` k `` _is a substring of_ `` s ``. Otherwise, return `` false ``.

 

__Example 1:__

```
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
```

__Example 2:__

```
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
```

__Example 3:__

```
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
```

 

__Constraints:__

*   <code>1 <= s.length <= 5 * 10<sup>5</sup></code>
*   `` s[i] `` is either `` '0' `` or `` '1' ``.
*   `` 1 <= k <= 20 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 174,746 | 99,326 | 56.8% |