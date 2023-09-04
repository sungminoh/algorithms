### [1744. Number of Ways to Form a Target String Given a Dictionary](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/?envType=daily-question&envId=2023-04-16)

Hard

You are given a list of strings of the __same length__ `` words `` and a string `` target ``.

Your task is to form `` target `` using the given `` words `` under the following rules:

*   `` target `` should be formed from left to right.
*   To form the <code>i<sup>th</sup></code> character (__0-indexed__) of `` target ``, you can choose the <code>k<sup>th</sup></code> character of the <code>j<sup>th</sup></code> string in `` words `` if `` target[i] = words[j][k] ``.
*   Once you use the <code>k<sup>th</sup></code> character of the <code>j<sup>th</sup></code> string of `` words ``, you __can no longer__ use the <code>x<sup>th</sup></code> character of any string in `` words `` where `` x <= k ``. In other words, all characters to the left of or at index `` k `` become unusuable for every string.
*   Repeat the process until you form the string `` target ``.

__Notice__ that you can use __multiple characters__ from the __same string__ in `` words `` provided the conditions above are met.

Return _the number of ways to form `` target `` from `` words ``_. Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("<u>a</u>cca"), index 1 ("b<u>b</u>bb"), index 3 ("cac<u>a</u>")
"aba" -> index 0 ("<u>a</u>cca"), index 2 ("bb<u>b</u>b"), index 3 ("cac<u>a</u>")
"aba" -> index 0 ("<u>a</u>cca"), index 1 ("b<u>b</u>bb"), index 3 ("acc<u>a</u>")
"aba" -> index 0 ("<u>a</u>cca"), index 2 ("bb<u>b</u>b"), index 3 ("acc<u>a</u>")
"aba" -> index 1 ("c<u>a</u>ca"), index 2 ("bb<u>b</u>b"), index 3 ("acc<u>a</u>")
"aba" -> index 1 ("c<u>a</u>ca"), index 2 ("bb<u>b</u>b"), index 3 ("cac<u>a</u>")
```

<strong class="example">Example 2:</strong>

```
Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("<u>b</u>aab"), index 1 ("b<u>a</u>ab"), index 2 ("ab<u>b</u>a")
"bab" -> index 0 ("<u>b</u>aab"), index 1 ("b<u>a</u>ab"), index 3 ("baa<u>b</u>")
"bab" -> index 0 ("<u>b</u>aab"), index 2 ("ba<u>a</u>b"), index 3 ("baa<u>b</u>")
"bab" -> index 1 ("a<u>b</u>ba"), index 2 ("ba<u>a</u>b"), index 3 ("baa<u>b</u>")
```

 

__Constraints:__

*   `` 1 <= words.length <= 1000 ``
*   `` 1 <= words[i].length <= 1000 ``
*   All strings in `` words `` have the same length.
*   `` 1 <= target.length <= 1000 ``
*   `` words[i] `` and `` target `` contain only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 97,360 | 51,477 | 52.9% |