### [483. Smallest Good Base](https://leetcode.com/problems/smallest-good-base/)

Hard

Given an integer `` n `` represented as a string, return _the smallest __good base__ of_ `` n ``.

We call `` k >= 2 `` a __good base__ of `` n ``, if all digits of `` n `` base `` k `` are `` 1 ``'s.

 

<strong class="example">Example 1:</strong>

```
Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.
```

<strong class="example">Example 2:</strong>

```
Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
```

<strong class="example">Example 3:</strong>

```
Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
```

 

__Constraints:__

*   `` n `` is an integer in the range <code>[3, 10<sup>18</sup>]</code>.
*   `` n `` does not contain any leading zeros.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 47,461 | 18,214 | 38.4% |