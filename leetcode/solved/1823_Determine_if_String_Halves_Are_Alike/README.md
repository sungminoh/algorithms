### [1823. Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12)

Easy

You are given a string `` s `` of even length. Split this string into two halves of equal lengths, and let `` a `` be the first half and `` b `` be the second half.

Two strings are __alike__ if they have the same number of vowels (`` 'a' ``, `` 'e' ``, `` 'i' ``, `` 'o' ``, `` 'u' ``, `` 'A' ``, `` 'E' ``, `` 'I' ``, `` 'O' ``, `` 'U' ``). Notice that `` s `` contains uppercase and lowercase letters.

Return `` true ``_ if _`` a ``_ and _`` b ``_ are __alike___. Otherwise, return `` false ``.

 

<strong class="example">Example 1:</strong>

```
Input: s = "book"
Output: true
Explanation: a = "b<u>o</u>" and b = "<u>o</u>k". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
```

<strong class="example">Example 2:</strong>

```
Input: s = "textbook"
Output: false
Explanation: a = "t<u>e</u>xt" and b = "b<u>oo</u>k". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
```

 

__Constraints:__

*   `` 2 <= s.length <= 1000 ``
*   `` s.length `` is even.
*   `` s `` consists of __uppercase and lowercase__ letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 426,878 | 336,214 | 78.8% |