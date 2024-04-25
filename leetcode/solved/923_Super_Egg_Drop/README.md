### [923. Super Egg Drop](https://leetcode.com/problems/super-egg-drop/description/)

Hard

You are given `` k `` identical eggs and you have access to a building with `` n `` floors labeled from `` 1 `` to `` n ``.

You know that there exists a floor `` f `` where `` 0 <= f <= n `` such that any egg dropped at a floor __higher__ than `` f `` will __break__, and any egg dropped __at or below__ floor `` f `` will __not break__.

Each move, you may take an unbroken egg and drop it from any floor `` x `` (where `` 1 <= x <= n ``). If the egg breaks, you can no longer use it. However, if the egg does not break, you may __reuse__ it in future moves.

Return _the __minimum number of moves__ that you need to determine __with certainty__ what the value of _`` f `` is.

 

<strong class="example">Example 1:</strong>

```
Input: k = 1, n = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
```

<strong class="example">Example 2:</strong>

```
Input: k = 2, n = 6
Output: 3
```

<strong class="example">Example 3:</strong>

```
Input: k = 3, n = 14
Output: 4
```

 

__Constraints:__

*   `` 1 <= k <= 100 ``
*   <code>1 <= n <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 255,476 | 70,633 | 27.6% |