### [1329. Minimum Cost to Move Chips to The Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)

Easy

We have `` n `` chips, where the position of the <code>i<sup>th</sup></code> chip is `` position[i] ``.

We need to move all the chips to __the same position__. In one step, we can change the position of the <code>i<sup>th</sup></code> chip from `` position[i] `` to:

*   `` position[i] + 2 `` or `` position[i] - 2 `` with `` cost = 0 ``.
*   `` position[i] + 1 `` or `` position[i] - 1 `` with `` cost = 1 ``.

Return _the minimum cost_ needed to move all the chips to the same position.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg" style="width: 750px; height: 217px;"/>

```
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg" style="width: 750px; height: 306px;"/>

```
Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
```

__Example 3:__

```
Input: position = [1,1000000000]
Output: 1
```

 

__Constraints:__

*   `` 1 <= position.length <= 100 ``
*   `` 1 <= position[i] <= 10^9 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 120,823 | 87,981 | 72.8% |