### [1035. Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/)

Easy

Given the `` root `` of a binary tree with unique values and the values of two different nodes of the tree `` x `` and `` y ``, return `` true `` _if the nodes corresponding to the values _`` x ``_ and _`` y ``_ in the tree are __cousins__, or _`` false ``_ otherwise._

Two nodes of a binary tree are __cousins__ if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth `` 0 ``, and children of each depth `` k `` node are at the depth `` k + 1 ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png" style="width: 304px; height: 270px;"/>

```
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png" style="width: 334px; height: 266px;"/>

```
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png" style="width: 267px; height: 258px;"/>

```
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [2, 100] ``.
*   `` 1 <= Node.val <= 100 ``
*   Each node has a __unique__ value.
*   `` x != y ``
*   `` x `` and `` y `` are exist in the tree.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 349,398 | 187,254 | 53.6% |