### [1343. Dice Roll Simulation](https://leetcode.com/problems/dice-roll-simulation/description/)

Hard

A die simulator generates a random number from `` 1 `` to `` 6 `` for each roll. You introduced a constraint to the generator such that it cannot roll the number `` i `` more than `` rollMax[i] `` (__1-indexed__) consecutive times.

Given an array of integers `` rollMax `` and an integer `` n ``, return _the number of distinct sequences that can be obtained with exact _`` n ``_ rolls_. Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

Two sequences are considered different if at least one element differs from each other.

 

<strong class="example">Example 1:</strong>

```
Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
```

<strong class="example">Example 2:</strong>

```
Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
```

<strong class="example">Example 3:</strong>

```
Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181
```

 

__Constraints:__

*   `` 1 <= n <= 5000 ``
*   `` rollMax.length == 6 ``
*   `` 1 <= rollMax[i] <= 15 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 59,523 | 29,186 | 49.0% |