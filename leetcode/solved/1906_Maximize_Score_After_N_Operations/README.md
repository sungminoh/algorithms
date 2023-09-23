### [1906. Maximize Score After N Operations](https://leetcode.com/problems/maximize-score-after-n-operations/?envType=daily-question&envId=2023-05-14)

Hard

You are given `` nums ``, an array of positive integers of size `` 2 * n ``. You must perform `` n `` operations on this array.

In the <code>i<sup>th</sup></code> operation __(1-indexed)__, you will:

*   Choose two elements, `` x `` and `` y ``.
*   Receive a score of `` i * gcd(x, y) ``.
*   Remove `` x `` and `` y `` from `` nums ``.

Return _the maximum score you can receive after performing _`` n ``_ operations._

The function `` gcd(x, y) `` is the greatest common divisor of `` x `` and `` y ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
```

<strong class="example">Example 2:</strong>

```
Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
```

 

__Constraints:__

*   `` 1 <= n <= 7 ``
*   `` nums.length == 2 * n ``
*   <code>1 <= nums[i] <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 95,944 | 55,952 | 58.3% |