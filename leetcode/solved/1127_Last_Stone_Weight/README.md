### [1127. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/?envType=daily-question&envId=2023-04-24)

Easy

You are given an array of integers `` stones `` where `` stones[i] `` is the weight of the <code>i<sup>th</sup></code> stone.

We are playing a game with the stones. On each turn, we choose the __heaviest two stones__ and smash them together. Suppose the heaviest two stones have weights `` x `` and `` y `` with `` x <= y ``. The result of this smash is:

*   If `` x == y ``, both stones are destroyed, and
*   If `` x != y ``, the stone of weight `` x `` is destroyed, and the stone of weight `` y `` has new weight `` y - x ``.

At the end of the game, there is __at most one__ stone left.

Return _the weight of the last remaining stone_. If there are no stones left, return `` 0 ``.

 

<strong class="example">Example 1:</strong>

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
```

<strong class="example">Example 2:</strong>

```
Input: stones = [1]
Output: 1
```

 

__Constraints:__

*   `` 1 <= stones.length <= 30 ``
*   `` 1 <= stones[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 791,592 | 516,358 | 65.2% |