### [942. Super Palindromes](https://leetcode.com/problems/super-palindromes/)

Hard

Let's say a positive integer is a __super-palindrome__ if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers `` left `` and `` right `` represented as strings, return _the number of __super-palindromes__ integers in the inclusive range_ `` [left, right] ``.

 

__Example 1:__

```
Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
```

__Example 2:__

```
Input: left = "1", right = "2"
Output: 1
```

 

__Constraints:__

*   `` 1 <= left.length, right.length <= 18 ``
*   `` left `` and `` right `` consist of only digits.
*   `` left `` and `` right `` cannot have leading zeros.
*   `` left `` and `` right `` represent integers in the range <code>[1, 10<sup>18</sup> - 1]</code>.
*   `` left `` is less than or equal to `` right ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 49,925 | 19,491 | 39.0% |