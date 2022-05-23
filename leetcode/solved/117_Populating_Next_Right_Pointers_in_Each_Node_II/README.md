### [117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

Medium

Given a binary tree

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `` NULL ``.

Initially, all next pointers are set to `` NULL ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" style="width: 500px; height: 171px;"/>

```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

__Example 2:__

```
Input: root = []
Output: []
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 6000] ``.
*   `` -100 <= Node.val <= 100 ``

 

__Follow-up:__

*   You may only use constant extra space.
*   The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 985,074 | 476,804 | 48.4% |