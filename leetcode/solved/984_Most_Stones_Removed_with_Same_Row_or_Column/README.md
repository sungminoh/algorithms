### [984. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

Medium

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a _move_ consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

<div>
<p><strong>Example 1:</strong></p>
```
Input: stones = <span id="example-input-1-2">[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]</span>
Output: 5
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: stones = <span id="example-input-2-2">[[0,0],[0,2],[1,1],[2,0],[2,2]]</span>
Output: 3
```
<div>
<p><strong>Example 3:</strong></p>
```
Input: stones = <span id="example-input-3-2">[[0,0]]</span>
Output: 0
```
<p> </p>
<p><strong><span>Note:</span></strong></p>
<ol>
<li><code>1 <= stones.length <= 1000</code></li>
<li><code>0 <= stones[i][j] < 10000</code></li>
</ol>
</div>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 85,584 | 47,315 | 55.3% |