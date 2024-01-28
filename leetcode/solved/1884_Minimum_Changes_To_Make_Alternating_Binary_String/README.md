### [1884. Minimum Changes To Make Alternating Binary String](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2023-12-24)

Easy

You are given a string `` s `` consisting only of the characters `` '0' `` and `` '1' ``. In one operation, you can change any `` '0' `` to `` '1' `` or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string `` "010" `` is alternating, while the string `` "0100" `` is not.

Return _the __minimum__ number of operations needed to make_ `` s `` _alternating_.

 

<strong class="example">Example 1:</strong>

```
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
```

<strong class="example">Example 2:</strong>

```
Input: s = "10"
Output: 0
Explanation: s is already alternating.
```

<strong class="example">Example 3:</strong>

```
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>4</sup></code>
*   `` s[i] `` is either `` '0' `` or `` '1' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 215,181 | 137,838 | 64.1% |