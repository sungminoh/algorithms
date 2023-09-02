### [2392. Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

Medium

You are given two positive integer arrays `` spells `` and `` potions ``, of length `` n `` and `` m `` respectively, where `` spells[i] `` represents the strength of the <code>i<sup>th</sup></code> spell and `` potions[j] `` represents the strength of the <code>j<sup>th</sup></code> potion.

You are also given an integer `` success ``. A spell and potion pair is considered __successful__ if the __product__ of their strengths is __at least__ `` success ``.

Return _an integer array _`` pairs ``_ of length _`` n ``_ where _`` pairs[i] ``_ is the number of __potions__ that will form a successful pair with the _<code>i<sup>th</sup></code>_ spell._

 

<strong class="example">Example 1:</strong>

```
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0<sup>th</sup> spell: 5 * [1,2,3,4,5] = [5,<u>10</u>,<u>15</u>,<u>20</u>,<u>25</u>]. 4 pairs are successful.
- 1<sup>st</sup> spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2<sup>nd</sup> spell: 3 * [1,2,3,4,5] = [3,6,<u>9</u>,<u>12</u>,<u>15</u>]. 3 pairs are successful.
Thus, [4,0,3] is returned.
```

<strong class="example">Example 2:</strong>

```
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0<sup>th</sup> spell: 3 * [8,5,8] = [<u>24</u>,15,<u>24</u>]. 2 pairs are successful.
- 1<sup>st</sup> spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2<sup>nd</sup> spell: 2 * [8,5,8] = [<u>16</u>,10,<u>16</u>]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
```

 

__Constraints:__

*   `` n == spells.length ``
*   `` m == potions.length ``
*   <code>1 <= n, m <= 10<sup>5</sup></code>
*   <code>1 <= spells[i], potions[i] <= 10<sup>5</sup></code>
*   <code>1 <= success <= 10<sup>10</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 218,146 | 90,168 | 41.3% |