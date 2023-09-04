### [1474. Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=daily-question&envId=2023-04-19)

Medium

You are given the `` root `` of a binary tree.

A ZigZag path for a binary tree is defined as follow:

*   Choose __any __node in the binary tree and a direction (right or left).
*   If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
*   Change the direction from right to left or from left to right.
*   Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return _the longest __ZigZag__ path contained in that tree_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/22/sample_1_1702.png" style="width: 221px; height: 383px;"/>

```
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/22/sample_2_1702.png" style="width: 157px; height: 329px;"/>

```
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
```

<strong class="example">Example 3:</strong>

```
Input: root = [1]
Output: 0
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.
*   `` 1 <= Node.val <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 175,625 | 117,279 | 66.8% |