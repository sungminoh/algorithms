### [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Medium

Given two integer arrays `` preorder `` and `` inorder `` where `` preorder `` is the preorder traversal of a binary tree and `` inorder `` is the inorder traversal of the same tree, construct and return _the binary tree_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;"/>

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

__Example 2:__

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

 

__Constraints:__

*   `` 1 <= preorder.length <= 3000 ``
*   `` inorder.length == preorder.length ``
*   `` -3000 <= preorder[i], inorder[i] <= 3000 ``
*   `` preorder `` and `` inorder `` consist of __unique__ values.
*   Each value of `` inorder `` also appears in `` preorder ``.
*   `` preorder `` is __guaranteed__ to be the preorder traversal of the tree.
*   `` inorder `` is __guaranteed__ to be the inorder traversal of the tree.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,006,054 | 545,338 | 54.2% |