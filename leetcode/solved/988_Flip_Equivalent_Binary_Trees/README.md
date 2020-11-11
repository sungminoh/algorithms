### [988. Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/)

Medium

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is _flip equivalent_ to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are _flip equivalent_.  The trees are given by root nodes `` root1 `` and `` root2 ``.

 

__Example 1:__

```
Input: root1 = <span id="example-input-1-1">[1,2,3,4,5,6,null,null,null,7,8]</span>, root2 = <span id="example-input-1-2">[1,3,2,null,6,4,5,null,null,null,null,8,7]</span>
Output: <span id="example-output-1">true</span>
Explanation: We flipped at nodes with values 1, 3, and 5.
<img alt="Flipped Trees Diagram" src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS"; width: 455px; height: 200px;'/>
```

 

__Note:__

1.   Each tree will have at most `` 100 `` nodes.
2.   Each value in each tree will be a unique integer in the range `` [0, 99] ``.

<div>
<p> </p>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 66,862 | 43,831 | 65.6% |