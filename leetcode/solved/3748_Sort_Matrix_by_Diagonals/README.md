### [3748. Sort Matrix by Diagonals](https://leetcode.com/problems/sort-matrix-by-diagonals/description/?envType=daily-question&envId=2025-08-28)

Medium

You are given an `` n x n `` square matrix of integers `` grid ``. Return the matrix such that:

*   The diagonals in the __bottom-left triangle__ (including the middle diagonal) are sorted in __non-increasing order__.
*   The diagonals in the __top-right triangle__ are sorted in __non-decreasing order__.

 

<strong class="example">Example 1:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,7,3],[9,8,2],[4,5,6]]</span></p>
<p><strong>Output:</strong> <span class="example-io">[[8,2,3],[9,6,7],[4,5,1]]</span></p>
<p><strong>Explanation:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/29/4052example1drawio.png" style="width: 461px; height: 181px;"/></p>
<p>The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:</p>
<ul>
<li><code>[1, 8, 6]</code> becomes <code>[8, 6, 1]</code>.</li>
<li><code>[9, 5]</code> and <code>[4]</code> remain unchanged.</li>
</ul>
<p>The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:</p>
<ul>
<li><code>[7, 2]</code> becomes <code>[2, 7]</code>.</li>
<li><code>[3]</code> remains unchanged.</li>
</ul>
</div>

<strong class="example">Example 2:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1],[1,2]]</span></p>
<p><strong>Output:</strong> <span class="example-io">[[2,1],[1,0]]</span></p>
<p><strong>Explanation:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/29/4052example2adrawio.png" style="width: 383px; height: 141px;"/></p>
<p>The diagonals with a black arrow must be non-increasing, so <code>[0, 2]</code> is changed to <code>[2, 0]</code>. The other diagonals are already in the correct order.</p>
</div>

<strong class="example">Example 3:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1]]</span></p>
<p><strong>Output:</strong> <span class="example-io">[[1]]</span></p>
<p><strong>Explanation:</strong></p>
<p>Diagonals with exactly one element are already in order, so no changes are needed.</p>
</div>

 

__Constraints:__

*   `` grid.length == grid[i].length == n ``
*   `` 1 <= n <= 10 ``
*   <code>-10<sup>5</sup> <= grid[i][j] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 148,638 | 125,982 | 84.8% |