### [1746. Largest Substring Between Two Equal Characters](https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=daily-question&envId=2023-12-31)

Easy

Given a string `` s ``, return _the length of the longest substring between two equal characters, excluding the two characters._ If there is no such substring return `` -1 ``.

A __substring__ is a contiguous sequence of characters within a string.

 

<strong class="example">Example 1:</strong>

<strong>Input:</strong> s = "aa"
    <strong>Output:</strong> 0
    <strong>Explanation:</strong> The optimal substring here is an empty substring between the two 'a's.

<strong class="example">Example 2:</strong>

```
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
```

<strong class="example">Example 3:</strong>

```
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
```

 

__Constraints:__

*   `` 1 <= s.length <= 300 ``
*   `` s `` contains only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 208,708 | 143,864 | 68.9% |