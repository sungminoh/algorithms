### [467. Unique Substrings in Wraparound String](https://leetcode.com/problems/unique-substrings-in-wraparound-string/)

Medium

Consider the string `` s `` to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so `` s `` will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string `` p ``. Your job is to find out how many unique non-empty substrings of `` p `` are present in `` s ``. In particular, your input is the string `` p `` and you need to output the number of different non-empty substrings of `` p `` in the string `` s ``.

__Note:__ `` p `` consists of only lowercase English letters and the size of p might be over 10000.

__Example 1:__  

```
<b>Input:</b> "a"
<b>Output:</b> 1

<b>Explanation:</b> Only the substring "a" of string "a" is in the string s.
```

__Example 2:__  

```
<b>Input:</b> "cac"
<b>Output:</b> 2
<b>Explanation:</b> There are two substrings "a", "c" of string "cac" in the string s.
```

__Example 3:__  

```
<b>Input:</b> "zab"
<b>Output:</b> 6
<b>Explanation:</b> There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 67,010 | 23,540 | 35.1% |