### [1567. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=daily-question&envId=2023-05-05)

Medium

Given a string `` s `` and an integer `` k ``, return _the maximum number of vowel letters in any substring of _`` s ``_ with length _`` k ``.

__Vowel letters__ in English are `` 'a' ``, `` 'e' ``, `` 'i' ``, `` 'o' ``, and `` 'u' ``.

 

<strong class="example">Example 1:</strong>

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

<strong class="example">Example 2:</strong>

```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

<strong class="example">Example 3:</strong>

```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists of lowercase English letters.
*   `` 1 <= k <= s.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 320,675 | 186,940 | 58.3% |