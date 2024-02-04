### [2346. Largest 3-Same-Digit Number in String](https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2023-12-04)

Easy

You are given a string `` num `` representing a large integer. An integer is __good__ if it meets the following conditions:

*   It is a __substring__ of `` num `` with length `` 3 ``.
*   It consists of only one unique digit.

Return _the __maximum good __integer as a __string__ or an empty string _`` "" ``_ if no such integer exists_.

Note:

*   A __substring__ is a contiguous sequence of characters within a string.
*   There may be __leading zeroes__ in `` num `` or a good integer.

 

<strong class="example">Example 1:</strong>

```
Input: num = "6<u>777</u>133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
```

<strong class="example">Example 2:</strong>

```
Input: num = "23<u>000</u>19"
Output: "000"
Explanation: "000" is the only good integer.
```

<strong class="example">Example 3:</strong>

```
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
```

 

__Constraints:__

*   `` 3 <= num.length <= 1000 ``
*   `` num `` only consists of digits.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 196,384 | 136,040 | 69.3% |