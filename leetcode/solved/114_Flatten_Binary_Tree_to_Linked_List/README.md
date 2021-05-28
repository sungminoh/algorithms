### [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

Medium

Given the `` root `` of a binary tree, flatten the tree into a "linked list":

*   The "linked list" should use the same `` TreeNode `` class where the `` right `` child pointer points to the next node in the list and the `` left `` child pointer is always `` null ``.
*   The "linked list" should be in the same order as a <a href="https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR" target="_blank">__pre-order____ traversal__</a> of the binary tree.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;"/>

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

__Example 2:__

```
Input: root = []
Output: []
```

__Example 3:__

```
Input: root = [0]
Output: [0]
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 2000] ``.
*   `` -100 <= Node.val <= 100 ``

 
__Follow up:__ Can you flatten the tree in-place (with `` O(1) `` extra space)?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 857,818 | 459,314 | 53.5% |