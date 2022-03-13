### [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)

Medium

Given the `` root `` of a binary tree, return _the __maximum width__ of the given tree_.

The __maximum width__ of a tree is the maximum __width__ among all levels.

The __width__ of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is __guaranteed__ that the answer will in the range of __32-bit__ signed integer.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg" style="width: 359px; height: 302px;"/>

```
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width2-tree.jpg" style="width: 224px; height: 302px;"/>

```
Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg" style="width: 289px; height: 299px;"/>

```
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 3000] ``.
*   `` -100 <= Node.val <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 435,111 | 174,701 | 40.2% |