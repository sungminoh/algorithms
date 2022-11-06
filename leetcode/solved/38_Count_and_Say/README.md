### [38. Count and Say](https://leetcode.com/problems/count-and-say/)

Medium

The __count-and-say__ sequence is a sequence of digit strings defined by the recursive formula:

*   `` countAndSay(1) = "1" ``
*   `` countAndSay(n) `` is the way you would "say" the digit string from `` countAndSay(n-1) ``, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the __minimal__ number of substrings such that each substring contains exactly __one__ unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string `` "3322251" ``:

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg" style="width: 581px; height: 172px;"/>

Given a positive integer `` n ``, return _the _<code>n<sup>th</sup></code>_ term of the __count-and-say__ sequence_.

 

<strong class="example">Example 1:</strong>

```
Input: n = 1
Output: "1"
Explanation: This is the base case.
```

<strong class="example">Example 2:</strong>

```
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
```

 

__Constraints:__

*   `` 1 <= n <= 30 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,436,110 | 736,314 | 51.3% |