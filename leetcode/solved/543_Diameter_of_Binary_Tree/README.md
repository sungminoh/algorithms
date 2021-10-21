### [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

Easy

Given the `` root `` of a binary tree, return _the length of the __diameter__ of the tree_.

The __diameter__ of a binary tree is the __length__ of the longest path between any two nodes in a tree. This path may or may not pass through the `` root ``.

The __length__ of a path between two nodes is represented by the number of edges between them.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" style="width: 292px; height: 302px;"/>

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

__Example 2:__

```
Input: root = [1,2]
Output: 1
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   `` -100 <= Node.val <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,124,311 | 587,209 | 52.2% |