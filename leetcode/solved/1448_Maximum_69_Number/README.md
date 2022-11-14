### [1448. Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/)

Easy

You are given a positive integer `` num `` consisting only of digits `` 6 `` and `` 9 ``.

Return _the maximum number you can get by changing __at most__ one digit (_`` 6 ``_ becomes _`` 9 ``_, and _`` 9 ``_ becomes _`` 6 ``_)_.

 

<strong class="example">Example 1:</strong>

```
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
```

<strong class="example">Example 2:</strong>

```
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
```

<strong class="example">Example 3:</strong>

```
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
```

 

__Constraints:__

*   <code>1 <= num <= 10<sup>4</sup></code>
*   `` num `` consists of only `` 6 `` and `` 9 `` digits.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 239,132 | 196,239 | 82.1% |