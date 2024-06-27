### [1675. Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/description/?envType=daily-question&envId=2024-06-20)

Medium

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has `` n `` empty baskets, the <code>i<sup>th</sup></code> basket is at `` position[i] ``, Morty has `` m `` balls and needs to distribute the balls into the baskets such that the __minimum magnetic force__ between any two balls is __maximum__.

Rick stated that magnetic force between two different balls at positions `` x `` and `` y `` is `` |x - y| ``.

Given the integer array `` position `` and the integer `` m ``. Return _the required force_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/11/q3v1.jpg" style="width: 562px; height: 195px;"/>

```
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
```

<strong class="example">Example 2:</strong>

```
Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
```

 

__Constraints:__

*   `` n == position.length ``
*   <code>2 <= n <= 10<sup>5</sup></code>
*   <code>1 <= position[i] <= 10<sup>9</sup></code>
*   All integers in `` position `` are __distinct__.
*   `` 2 <= m <= position.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 225,653 | 160,259 | 71.0% |