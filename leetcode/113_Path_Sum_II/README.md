### [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

Medium

Given the `` root `` of a binary tree and an integer `` targetSum ``, return _all __root-to-leaf__ paths where the sum of the node values in the path equals _`` targetSum ``_. Each path should be returned as a list of the node __values__, not node references_.

A __root-to-leaf__ path is a path starting from the root and ending at any leaf node. A __leaf__ is a node with no children.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" style="width: 500px; height: 356px;"/>

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" style="width: 212px; height: 181px;"/>

```
Input: root = [1,2,3], targetSum = 5
Output: []
```

<strong class="example">Example 3:</strong>

```
Input: root = [1,2], targetSum = 0
Output: []
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 5000] ``.
*   `` -1000 <= Node.val <= 1000 ``
*   `` -1000 <= targetSum <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,228,260 | 694,719 | 56.6% |