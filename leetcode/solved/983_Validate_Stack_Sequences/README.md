### [983. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)

Medium

Given two sequences `` pushed `` and `` popped `` __with distinct values__, return `` true `` if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

<div>
<p><strong>Example 1:</strong></p>
```
Input: pushed = <span id="example-input-1-1">[1,2,3,4,5]</span>, popped = <span id="example-input-1-2">[4,5,3,2,1]</span>
Output: <span id="example-output-1">true</span>
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: pushed = <span id="example-input-2-1">[1,2,3,4,5]</span>, popped = <span id="example-input-2-2">[4,3,5,1,2]</span>
Output: <span id="example-output-2">false</span>
Explanation: 1 cannot be popped before 2.
```
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>0 <= pushed.length == popped.length <= 1000</code></li>
<li><code>0 <= pushed[i], popped[i] < 1000</code></li>
<li><code>pushed</code> is a permutation of <code>popped</code>.</li>
<li><code>pushed</code> and <code>popped</code> have distinct values.</li>
</ol>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 62,368 | 37,649 | 60.4% |