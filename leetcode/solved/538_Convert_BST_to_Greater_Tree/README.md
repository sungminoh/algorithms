### [538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)

Medium

Given the `` root `` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a _binary search tree_ is a tree that satisfies these constraints:

*   The left subtree of a node contains only nodes with keys __less than__ the node's key.
*   The right subtree of a node contains only nodes with keys __greater than__ the node's key.
*   Both the left and right subtrees must also be binary search trees.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/02/tree.png" style="width: 500px; height: 341px;"/>

```
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

__Example 2:__

```
Input: root = [0,null,1]
Output: [1,null,1]
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code>
*   All the values in the tree are __unique__.
*   `` root `` is guaranteed to be a valid binary search tree.

 

__Note:__ This question is the same as 1038: <a href="https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/" target="_blank">https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/</a>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 359,930 | 238,209 | 66.2% |