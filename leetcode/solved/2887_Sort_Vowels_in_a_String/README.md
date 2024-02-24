### [2887. Sort Vowels in a String](https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2023-11-13)

Medium

Given a __0-indexed__ string `` s ``, __permute__ `` s `` to get a new string `` t `` such that:

*   All consonants remain in their original places. More formally, if there is an index `` i `` with `` 0 <= i < s.length `` such that `` s[i] `` is a consonant, then `` t[i] = s[i] ``.
*   The vowels must be sorted in the __nondecreasing__ order of their __ASCII__ values. More formally, for pairs of indices `` i ``, `` j `` with `` 0 <= i < j < s.length `` such that `` s[i] `` and `` s[j] `` are vowels, then `` t[i] `` must not have a higher ASCII value than `` t[j] ``.

Return _the resulting string_.

The vowels are `` 'a' ``, `` 'e' ``, `` 'i' ``, `` 'o' ``, and `` 'u' ``, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

 

<strong class="example">Example 1:</strong>

```
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
```

<strong class="example">Example 2:</strong>

```
Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists only of letters of the English alphabet in __uppercase and lowercase__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 144,972 | 118,650 | 81.8% |