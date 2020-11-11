### [992. Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/)

Medium

We are given an array `` A `` of `` N `` lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array `` A = ["abcdef","uvwxyz"] `` and deletion indices `` {0, 2, 3} ``, then the final array after deletions is `` ["bef","vyz"] ``.

Suppose we chose a set of deletion indices `` D `` such that after deletions, the final array has its elements in __lexicographic__ order (`` A[0] <= A[1] <= A[2] ... <= A[A.length - 1] ``).

Return the minimum possible value of `` D.length ``.

 

<div>
<div>
<ol>
</ol>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>
```
Input: <span id="example-input-1-1">["ca","bb","ac"]</span>
Output: <span id="example-output-1">1</span>
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
```
<div>
<p><strong>Example 2:</strong></p>
```
Input: <span>["xc","yb","za"]</span>
Output: <span id="example-output-2">0</span>
Explanation: 
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
```
<div>
<p><strong>Example 3:</strong></p>
```
Input: <span id="example-input-3-1">["zyx","wvu","tsr"]</span>
Output: <span id="example-output-3">3</span>
Explanation: 
We have to delete every column.
```
<p> </p>
<div>
<div>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 <= A.length <= 100</code></li>
<li><code>1 <= A[i].length <= 100</code></li>
</ol>
</div>
</div>
</div>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 27,716 | 9,127 | 32.9% |