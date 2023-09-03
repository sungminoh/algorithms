### [2470. Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/?envType=daily-question&envId=2023-04-11)

Medium

You are given a string `` s ``, which contains stars `` * ``.

In one operation, you can:

*   Choose a star in `` s ``.
*   Remove the closest __non-star__ character to its __left__, as well as remove the star itself.

Return _the string after __all__ stars have been removed_.

__Note:__

*   The input will be generated such that the operation is always possible.
*   It can be shown that the resulting string will always be unique.

 

<strong class="example">Example 1:</strong>

```
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1<sup>st</sup> star is 't' in "lee<u>t</u>**cod*e". s becomes "lee*cod*e".
- The closest character to the 2<sup>nd</sup> star is 'e' in "le<u>e</u>*cod*e". s becomes "lecod*e".
- The closest character to the 3<sup>rd</sup> star is 'd' in "leco<u>d</u>*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
```

<strong class="example">Example 2:</strong>

```
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>5</sup></code>
*   `` s `` consists of lowercase English letters and stars `` * ``.
*   The operation above can be performed on `` s ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 231,346 | 169,203 | 73.1% |