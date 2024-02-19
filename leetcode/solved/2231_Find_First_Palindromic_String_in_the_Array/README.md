### [2231. Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=daily-question&envId=2024-02-13)

Easy

Given an array of strings `` words ``, return _the first __palindromic__ string in the array_. If there is no such string, return _an __empty string__ _`` "" ``.

A string is __palindromic__ if it reads the same forward and backward.

 

<strong class="example">Example 1:</strong>

```
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
```

<strong class="example">Example 2:</strong>

```
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
```

<strong class="example">Example 3:</strong>

```
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
```

 

__Constraints:__

*   `` 1 <= words.length <= 100 ``
*   `` 1 <= words[i].length <= 100 ``
*   `` words[i] `` consists only of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 300,048 | 252,172 | 84.0% |