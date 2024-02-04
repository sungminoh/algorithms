### [2032. Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=daily-question&envId=2023-12-07)

Easy

You are given a string `` num ``, representing a large integer. Return _the __largest-valued odd__ integer (as a string) that is a __non-empty substring__ of _`` num ``_, or an empty string _`` "" ``_ if no odd integer exists_.

A __substring__ is a contiguous sequence of characters within a string.

 

<strong class="example">Example 1:</strong>

```
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
```

<strong class="example">Example 2:</strong>

```
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
```

<strong class="example">Example 3:</strong>

```
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
```

 

__Constraints:__

*   <code>1 <= num.length <= 10<sup>5</sup></code>
*   `` num `` only consists of digits and does not contain any leading zeros.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 340,717 | 216,299 | 63.5% |