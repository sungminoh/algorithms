### [884. K-Similar Strings](https://leetcode.com/problems/k-similar-strings/description/)

Hard

Strings `` s1 `` and `` s2 `` are `` k ``__-similar__ (for some non-negative integer `` k ``) if we can swap the positions of two letters in `` s1 `` exactly `` k `` times so that the resulting string equals `` s2 ``.

Given two anagrams `` s1 `` and `` s2 ``, return the smallest `` k `` for which `` s1 `` and `` s2 `` are `` k ``__-similar__.

 

<strong class="example">Example 1:</strong>

```
Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
```

<strong class="example">Example 2:</strong>

```
Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".
```

 

__Constraints:__

*   `` 1 <= s1.length <= 20 ``
*   `` s2.length == s1.length ``
*   `` s1 `` and `` s2 `` contain only lowercase letters from the set `` {'a', 'b', 'c', 'd', 'e', 'f'} ``.
*   `` s2 `` is an anagram of `` s1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 113,993 | 45,345 | 39.8% |