### [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

Medium

Given a string, sort it in decreasing order based on the frequency of characters.

__Example 1:__

```
<b>Input:</b>
"tree"

<b>Output:</b>
"eert"

<b>Explanation:</b>
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

__Example 2:__

```
<b>Input:</b>
"cccaaa"

<b>Output:</b>
"cccaaa"

<b>Explanation:</b>
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```

__Example 3:__

```
<b>Input:</b>
"Aabb"

<b>Output:</b>
"bbAa"

<b>Explanation:</b>
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 233,891 | 139,642 | 59.7% |