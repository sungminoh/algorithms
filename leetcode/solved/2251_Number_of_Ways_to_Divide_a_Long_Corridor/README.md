### [2251. Number of Ways to Divide a Long Corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2023-11-28)

Hard

Along a long library corridor, there is a line of seats and decorative plants. You are given a __0-indexed__ string `` corridor `` of length `` n `` consisting of letters `` 'S' `` and `` 'P' `` where each `` 'S' `` represents a seat and each `` 'P' `` represents a plant.

One room divider has __already__ been installed to the left of index `` 0 ``, and __another__ to the right of index `` n - 1 ``. Additional room dividers can be installed. For each position between indices `` i - 1 `` and `` i `` (`` 1 <= i <= n - 1 ``), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has __exactly two seats__ with any number of plants. There may be multiple ways to perform the division. Two ways are __different__ if there is a position with a room divider installed in the first way but not in the second way.

Return _the number of ways to divide the corridor_. Since the answer may be very large, return it __modulo__ <code>10<sup>9</sup> + 7</code>. If there is no way, return `` 0 ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/1.png" style="width: 410px; height: 199px;"/>

```
Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/2.png" style="width: 357px; height: 68px;"/>

```
Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/12/3.png" style="width: 115px; height: 68px;"/>

```
Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
```

 

__Constraints:__

*   `` n == corridor.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   `` corridor[i] `` is either `` 'S' `` or `` 'P' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 132,098 | 65,624 | 49.7% |