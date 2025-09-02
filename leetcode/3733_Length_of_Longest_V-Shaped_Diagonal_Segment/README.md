### [3733. Length of Longest V-Shaped Diagonal Segment](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/description/?envType=daily-question&envId=2025-08-27)

Hard

You are given a 2D integer matrix `` grid `` of size `` n x m ``, where each element is either `` 0 ``, `` 1 ``, or `` 2 ``.

A __V-shaped diagonal segment__ is defined as:

*   The segment starts with `` 1 ``.
*   The subsequent elements follow this infinite sequence: `` 2, 0, 2, 0, ... ``.
*   The segment:	
    
    *   Starts __along__ a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
    *   Continues the__ sequence__ in the same diagonal direction.
    *   Makes__ at most one clockwise 90-degree____ turn__ to another diagonal direction while __maintaining__ the sequence.
    
    
    

Return the __length__ of the __longest__ __V-shaped diagonal segment__. If no valid segment _exists_, return 0.

 

<strong class="example">Example 1:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]</span></p>
<p><strong>Output:</strong> <span class="example-io">5</span></p>
<p><strong>Explanation:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/09/matrix_1-2.jpg" style="width: 201px; height: 192px;"/></p>
<p>The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: <code>(0,2) → (1,3) → (2,4)</code>, takes a <strong>90-degree clockwise turn</strong> at <code>(2,4)</code>, and continues as <code>(3,3) → (4,2)</code>.</p>
</div>

<strong class="example">Example 2:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]</span></p>
<p><strong>Output:</strong> <span class="example-io">4</span></p>
<p><strong>Explanation:</strong></p>
<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/12/09/matrix_2.jpg" style="width: 201px; height: 201px;"/></strong></p>
<p>The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: <code>(2,3) → (3,2)</code>, takes a <strong>90-degree clockwise turn</strong> at <code>(3,2)</code>, and continues as <code>(2,1) → (1,0)</code>.</p>
</div>

<strong class="example">Example 3:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]</span></p>
<p><strong>Output:</strong> <span class="example-io">5</span></p>
<p><strong>Explanation:</strong></p>
<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/12/09/matrix_3.jpg" style="width: 201px; height: 201px;"/></strong></p>
<p>The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: <code>(0,0) → (1,1) → (2,2) → (3,3) → (4,4)</code>.</p>
</div>

<strong class="example">Example 4:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1]]</span></p>
<p><strong>Output:</strong> <span class="example-io">1</span></p>
<p><strong>Explanation:</strong></p>
<p>The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: <code>(0,0)</code>.</p>
</div>

 

__Constraints:__

*   `` n == grid.length ``
*   `` m == grid[i].length ``
*   `` 1 <= n, m <= 500 ``
*   `` grid[i][j] `` is either `` 0 ``, `` 1 `` or `` 2 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 124,174 | 70,442 | 56.7% |