### [1050. Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

Medium

Given an array of integers preorder, which represents the __preorder traversal__ of a BST (i.e., __binary search tree__), construct the tree and return _its root_.

It is __guaranteed__ that there is always possible to find a binary search tree with the given requirements for the given test cases.

A __binary search tree__ is a binary tree where for every node, any descendant of `` Node.left `` has a value __strictly less than__ `` Node.val ``, and any descendant of `` Node.right `` has a value __strictly greater than__ `` Node.val ``.

A __preorder traversal__ of a binary tree displays the value of the node first, then traverses `` Node.left ``, then traverses `` Node.right ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/03/06/1266.png" style="height: 386px; width: 590px;"/>

```
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
```

__Example 2:__

```
Input: preorder = [1,3]
Output: [1,null,3]
```

 

__Constraints:__

*   `` 1 <= preorder.length <= 100 ``
*   `` 1 <= preorder[i] <= 1000 ``
*   All the values of `` preorder `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 255,033 | 203,368 | 79.7% |