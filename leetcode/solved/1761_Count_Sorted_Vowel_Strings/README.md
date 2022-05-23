### [1761. Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/)

Medium

Given an integer `` n ``, return _the number of strings of length _`` n ``_ that consist only of vowels (_`` a ``_, _`` e ``_, _`` i ``_, _`` o ``_, _`` u ``_) and are __lexicographically sorted__._

A string `` s `` is __lexicographically sorted__ if for all valid `` i ``, `` s[i] `` is the same as or comes before `` s[i+1] `` in the alphabet.

 

__Example 1:__

<strong>Input:</strong> n = 1
    <strong>Output:</strong> 5
    <strong>Explanation:</strong> The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

__Example 2:__

```
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
```

__Example 3:__

```
Input: n = 33
Output: 66045
```

 

__Constraints:__

*   `` 1 <= n <= 50 `` 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 169,420 | 131,422 | 77.6% |