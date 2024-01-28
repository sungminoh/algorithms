### [2025. Redistribute Characters to Make All Strings Equal](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/?envType=daily-question&envId=2023-12-30)

Easy

You are given an array of strings `` words `` (__0-indexed__).

In one operation, pick two __distinct__ indices `` i `` and `` j ``, where `` words[i] `` is a non-empty string, and move __any__ character from `` words[i] `` to __any__ position in `` words[j] ``.

Return `` true `` _if you can make__ every__ string in _`` words ``_ __equal __using __any__ number of operations_,_ and _`` false `` _otherwise_.

 

<strong class="example">Example 1:</strong>

<strong>Input:</strong> words = ["abc","aabc","bc"]
    <strong>Output:</strong> true
    <strong>Explanation:</strong> Move the first 'a' in words[1] to the front of words[2],
    to make <code>words[1]</code> = "abc" and words[2] = "abc".
    All the strings are now equal to "abc", so return <code>true</code>.

<strong class="example">Example 2:</strong>

```
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
```

 

__Constraints:__

*   `` 1 <= words.length <= 100 ``
*   `` 1 <= words[i].length <= 100 ``
*   `` words[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 191,732 | 130,106 | 67.9% |