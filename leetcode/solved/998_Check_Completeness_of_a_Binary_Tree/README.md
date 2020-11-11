### [998. Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)

Medium

Given a binary tree, determine if it is a _complete binary tree_.

<u>__Definition of a complete binary tree from <a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>:__</u>  
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2<sup>h</sup> nodes inclusive at the last level h.

 

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png" style="width: 180px; height: 145px;"/></strong>

```
Input: <span id="example-input-1-1">[1,2,3,4,5,6]</span>
Output: <span id="example-output-1">true</span>
<span>Explanation: </span>Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

<div>
<p><strong>Example 2:</strong></p>
<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png" style="width: 200px; height: 145px;"/></strong></p>
```
Input: <span id="example-input-2-1">[1,2,3,4,5,null,7]</span>
Output: <span id="example-output-2">false</span>
Explanation: The node with value 7 isn't as far left as possible.<span>
</span>
```
<div> </div>
</div>

__Note:__

1.   The tree will have between 1 and 100 nodes.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 91,702 | 47,390 | 51.7% |