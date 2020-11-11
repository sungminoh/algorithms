### [999. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/)

Medium

In a N x N `` grid `` composed of 1 x 1 squares, each 1 x 1 square consists of a `` / ``, `` \ ``, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a `` \ `` is represented as `` "\\" ``.)

Return the number of regions.

 

<div>
<div>
<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>
```
Input:
<span id="example-input-1-1">[
  " /",
  "/ "
]</span>
Output: <span id="example-output-1">2</span>
Explanation: The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/1.png" style="width: 82px; height: 82px;"/>
```
<div>
<p><strong>Example 2:</strong></p>
```
Input:
<span id="example-input-2-1">[
  " /",
  "  "
]</span>
Output: <span id="example-output-2">1</span>
Explanation: The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/2.png" style="width: 82px; height: 82px;"/>
```
<div>
<p><strong>Example 3:</strong></p>
```
Input:
<span id="example-input-3-1">[
  "\\/",
  "/\\"
]</span>
Output: <span id="example-output-3">4</span>
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/3.png" style="width: 82px; height: 82px;"/>
```
<div>
<p><strong>Example 4:</strong></p>
```
Input:
<span id="example-input-4-1">[
  "/\\",
  "\\/"
]</span>
Output: <span id="example-output-4">5</span>
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/4.png" style="width: 82px; height: 82px;"/>
```
<div>
<p><strong>Example 5:</strong></p>
```
Input:
<span id="example-input-5-1">[
  "//",
  "/ "
]</span>
Output: <span id="example-output-5">3</span>
Explanation: The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/5.png" style="width: 82px; height: 82px;"/>
```
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 <= grid.length == grid[0].length <= 30</code></li>
<li><code>grid[i][j]</code> is either <code>'/'</code>, <code>'\'</code>, or <code>' '</code>.</li>
</ol>
</div>
</div>
</div>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 25,507 | 16,805 | 65.9% |