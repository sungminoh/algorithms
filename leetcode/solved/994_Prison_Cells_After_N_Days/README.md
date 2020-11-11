### [994. Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/)

Medium

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

*   If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
*   Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: `` cells[i] == 1 `` if the `` i ``-th cell is occupied, else `` cells[i] == 0 ``.

Given the initial state of the prison, return the state of the prison after `` N `` days (and `` N `` such changes described above.)

 

<div>
<ol>
</ol>
</div>

<div>
<p><strong>Example 1:</strong></p>
```
Input: cells = <span id="example-input-1-1">[0,1,0,1,1,0,0,1]</span>, N = <span id="example-input-1-2">7</span>
Output: <span id="example-output-1">[0,0,1,1,0,0,0,0]</span>
Explanation: 
<span id="example-output-1">The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]</span>

```
<div>
<p><strong>Example 2:</strong></p>
```
Input: cells = <span id="example-input-2-1">[1,0,0,1,0,0,1,0]</span>, N = <span id="example-input-2-2">1000000000</span>
Output: <span id="example-output-2">[0,0,1,1,1,1,1,0]</span>
```
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>cells.length == 8</code></li>
<li><code>cells[i]</code> is in <code>{0, 1}</code></li>
<li><code>1 <= N <= 10^9</code></li>
</ol>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 124,393 | 49,261 | 39.6% |