### [2163. Kth Distinct String in an Array](https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=daily-question&envId=2024-08-05)

Easy

A __distinct string__ is a string that is present only __once__ in an array.

Given an array of strings `` arr ``, and an integer `` k ``, return _the _<code>k<sup>th</sup></code>_ __distinct string__ present in _`` arr ``. If there are __fewer__ than `` k `` distinct strings, return _an __empty string ___`` "" ``.

Note that the strings are considered in the __order in which they appear__ in the array.

 

<strong class="example">Example 1:</strong>

```
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1<sup>st</sup>, so it is the 1<sup>st</sup> distinct string.
"a" appears 2<sup>nd</sup>, so it is the 2<sup>nd</sup> distinct string.
Since k == 2, "a" is returned. 
```

<strong class="example">Example 2:</strong>

```
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1<sup>st</sup> string "aaa" is returned.
```

<strong class="example">Example 3:</strong>

```
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
```

 

__Constraints:__

*   `` 1 <= k <= arr.length <= 1000 ``
*   `` 1 <= arr[i].length <= 5 ``
*   `` arr[i] `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 286,540 | 235,224 | 82.1% |