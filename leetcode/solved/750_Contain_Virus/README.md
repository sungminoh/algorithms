### [750. Contain Virus](https://leetcode.com/problems/contain-virus/description/)

Hard

A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an `` m x n `` binary grid `` isInfected ``, where `` isInfected[i][j] == 0 `` represents uninfected cells, and `` isInfected[i][j] == 1 `` represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two __4-directionally__ adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There __will never be a tie__.

Return _the number of walls used to quarantine all the infected regions_. If the world will become fully infected, return the number of walls used.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/01/virus11-grid.jpg" style="width: 500px; height: 255px;"/>

```
Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/01/virus12edited-grid.jpg" style="width: 500px; height: 257px;"/>
On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/01/virus13edited-grid.jpg" style="width: 500px; height: 261px;"/>
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/01/virus2-grid.jpg" style="width: 653px; height: 253px;"/>

```
Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
```

<strong class="example">Example 3:</strong>

```
Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
```

 

__Constraints:__

*   `` m == isInfected.length ``
*   `` n == isInfected[i].length ``
*   `` 1 <= m, n <= 50 ``
*   `` isInfected[i][j] `` is either `` 0 `` or `` 1 ``.
*   There is always a contiguous viral region throughout the described process that will __infect strictly more uncontaminated squares__ in the next round.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 24,150 | 12,272 | 50.8% |