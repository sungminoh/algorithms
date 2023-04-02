### [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

Medium

Given the `` root `` of a binary tree, return _the zigzag level order traversal of its nodes' values_. (i.e., from left to right, then right to left for the next level and alternate between).

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;"/>

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

<strong class="example">Example 2:</strong>

```
Input: root = [1]
Output: [[1]]
```

<strong class="example">Example 3:</strong>

```
Input: root = []
Output: []
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 2000] ``.
*   `` -100 <= Node.val <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,648,367 | 936,798 | 56.8% |