### [991. Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/)

Medium

Given an array of integers `` A `` with even length, return `` true `` if and only if it is possible to reorder it such that `` A[2 * i + 1] = 2 * A[2 * i] `` for every `` 0 <= i < len(A) / 2 ``.

 

<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>
```
Input: <span id="example-input-1-1">[3,1,3,6]</span>
Output: <span id="example-output-1">false</span>
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: <span id="example-input-2-1">[2,1,2,6]</span>
Output: <span id="example-output-2">false</span>
```
<div>
<p><strong>Example 3:</strong></p>
```
Input: <span id="example-input-3-1">[4,-2,2,-4]</span>
Output: <span id="example-output-3">true</span>
Explanation: <span id="example-output-3">We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].</span>
```
<div>
<p><strong>Example 4:</strong></p>
```
Input: <span id="example-input-4-1">[1,2,4,16,8,4]</span>
Output: <span id="example-output-4">false</span>
```
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>0 <= A.length <= 30000</code></li>
<li><code>A.length</code> is even</li>
<li><code>-100000 <= A[i] <= 100000</code></li>
</ol>
</div>
</div>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 48,069 | 17,005 | 35.4% |