### [72. Edit Distance](https://leetcode.com/problems/edit-distance/)

Hard

Given two strings `` word1 `` and `` word2 ``, return _the minimum number of operations required to convert `` word1 `` to `` word2 ``_.

You have the following three operations permitted on a word:

*   Insert a character
*   Delete a character
*   Replace a character

 

<strong class="example">Example 1:</strong>

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

<strong class="example">Example 2:</strong>

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

 

__Constraints:__

*   `` 0 <= word1.length, word2.length <= 500 ``
*   `` word1 `` and `` word2 `` consist of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,165,587 | 634,244 | 54.4% |