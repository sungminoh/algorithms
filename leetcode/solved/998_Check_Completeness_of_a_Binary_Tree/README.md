### [998. Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)

Medium

Given the `` root `` of a binary tree, determine if it is a _complete binary tree_.

In a __<a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">complete binary tree</a>__, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between `` 1 `` and <code>2<sup>h</sup></code> nodes inclusive at the last level `` h ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png" style="width: 180px; height: 145px;"/>

```
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png" style="width: 200px; height: 145px;"/>

```
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 100] ``.
*   `` 1 <= Node.val <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 349,014 | 196,102 | 56.2% |