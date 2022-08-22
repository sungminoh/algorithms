### [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

Hard

You are given a string `` s `` and an array of strings `` words ``. All the strings of `` words `` are of __the same length__.

A __concatenated substring__ in `` s `` is a substring that contains all the strings of any permutation of `` words `` concatenated.

*   For example, if `` words = ["ab","cd","ef"] ``, then `` "abcdef" ``, `` "abefcd" ``, `` "cdabef" ``, `` "cdefab" ``, `` "efabcd" ``, and `` "efcdab" `` are all concatenated strings. `` "acdbef" `` is not a concatenated substring because it is not the concatenation of any permutation of `` words ``.

Return _the starting indices of all the concatenated substrings in _`` s ``. You can return the answer in __any order__.

 

__Example 1:__

```
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
```

__Example 2:__

```
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.
```

__Example 3:__

```
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>4</sup></code>
*   `` 1 <= words.length <= 5000 ``
*   `` 1 <= words[i].length <= 30 ``
*   `` s `` and `` words[i] `` consist of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,009,132 | 309,145 | 30.6% |