### [953. Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)

Easy

Given a string `` s ``, reverse the string according to the following rules:

*   All the characters that are not English letters remain in the same position.
*   All the English letters (lowercase or uppercase) should be reversed.

Return `` s ``_ after reversing it_.

 

__Example 1:__

```Input: s = "ab-cd"
Output: "dc-ba"
```

__Example 2:__

```Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```

__Example 3:__

```Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
```

 

__Constraints:__

*   `` 1 <= s.length <= 100 ``
*   `` s `` consists of characters with ASCII values in the range `` [33, 122] ``.
*   `` s `` does not contain `` '\"' `` or `` '\\' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 194,535 | 117,774 | 60.5% |