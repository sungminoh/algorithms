### [2562. Count Ways To Build Good Strings](https://leetcode.com/problems/count-ways-to-build-good-strings/?envType=daily-question&envId=2023-05-13)

Medium

Given the integers `` zero ``, `` one ``, `` low ``, and `` high ``, we can construct a string by starting with an empty string, and then at each step perform either of the following:

*   Append the character `` '0' `` `` zero `` times.
*   Append the character `` '1' `` `` one `` times.

This can be performed any number of times.

A __good__ string is a string constructed by the above process having a __length__ between `` low `` and `` high `` (__inclusive__).

Return _the number of __different__ good strings that can be constructed satisfying these properties._ Since the answer can be large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
```

<strong class="example">Example 2:</strong>

```
Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
```

 

__Constraints:__

*   <code>1 <= low <= high <= 10<sup>5</sup></code>
*   `` 1 <= zero, one <= low ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 118,238 | 65,677 | 55.5% |