### [564. Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/description/?envType=daily-question&envId=2024-08-24)

Hard

Given a string `` n `` representing an integer, return _the closest integer (not including itself), which is a palindrome_. If there is a tie, return ___the smaller one___.

The closest is defined as the absolute difference minimized between two integers.

 

<strong class="example">Example 1:</strong>

```
Input: n = "123"
Output: "121"
```

<strong class="example">Example 2:</strong>

```
Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
```

 

__Constraints:__

*   `` 1 <= n.length <= 18 ``
*   `` n `` consists of only digits.
*   `` n `` does not have leading zeros.
*   `` n `` is representing an integer in the range <code>[1, 10<sup>18</sup> - 1]</code>.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 380,650 | 120,541 | 31.7% |