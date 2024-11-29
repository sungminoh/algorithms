### [664. Strange Printer](https://leetcode.com/problems/strange-printer/description/?envType=daily-question&envId=2024-08-21)

Hard

There is a strange printer with the following two special properties:

*   The printer can only print a sequence of __the same character__ each time.
*   At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string `` s ``, return _the minimum number of turns the printer needed to print it_.

 

<strong class="example">Example 1:</strong>

```
Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
```

<strong class="example">Example 2:</strong>

```
Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
```

 

__Constraints:__

*   `` 1 <= s.length <= 100 ``
*   `` s `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 243,280 | 148,510 | 61.0% |