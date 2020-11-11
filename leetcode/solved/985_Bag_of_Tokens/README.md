### [985. Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)

Medium

You have an initial power `` P ``, an initial score of `` 0 `` points, and a bag of tokens.

Each token can be used at most once, has a value `` token[i] ``, and has potentially two ways to use it.

*   If we have at least `` token[i] `` power, we may play the token face up, losing `` token[i] `` power, and gaining `` 1 `` point.
*   If we have at least `` 1 `` point, we may play the token face down, gaining `` token[i] `` power, and losing `` 1 `` point.

Return the largest number of points we can have after playing any number of tokens.

 

<div>
<p><strong>Example 1:</strong></p>
```
Input: tokens = <span id="example-input-1-1">[100]</span>, P = <span id="example-input-1-2">50</span>
Output: <span id="example-output-1">0</span>
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: tokens = <span id="example-input-2-1">[100,200]</span>, P = <span id="example-input-2-2">150</span>
Output: <span id="example-output-2">1</span>
```
<div>
<p><strong>Example 3:</strong></p>
```
Input: tokens = <span id="example-input-3-1">[100,200,300,400]</span>, P = <span id="example-input-3-2">200</span>
Output: <span id="example-output-3">2</span>
```
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>tokens.length <= 1000</code></li>
<li><code>0 <= tokens[i] < 10000</code></li>
<li><code>0 <= P < 10000</code></li>
</ol>
</div>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 27,845 | 11,241 | 40.4% |