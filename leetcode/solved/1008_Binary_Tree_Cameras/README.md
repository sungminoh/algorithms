### [1008. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)

Hard

You are given the `` root `` of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return _the minimum number of cameras needed to monitor all nodes of the tree_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png" style="width: 138px; height: 163px;"/>

```
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png" style="width: 139px; height: 312px;"/>

```
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 1000] ``.
*   `` Node.val == 0 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 115,616 | 46,798 | 40.5% |