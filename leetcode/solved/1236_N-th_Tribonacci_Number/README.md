### [1236. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

Easy

The Tribonacci sequence T<sub>n</sub> is defined as follows: 

T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n >= 0.

Given `` n ``, return the value of T<sub>n</sub>.

 

<strong class="example">Example 1:</strong>

```
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

<strong class="example">Example 2:</strong>

```
Input: n = 25
Output: 1389537
```

 

__Constraints:__

*   `` 0 <= n <= 37 ``
*   The answer is guaranteed to fit within a 32-bit integer, ie. `` answer <= 2^31 - 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 733,241 | 467,578 | 63.8% |