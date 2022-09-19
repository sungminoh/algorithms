### [832. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

Medium

Given the `` root `` of a binary tree, return _the same tree where every subtree (of the given tree) not containing a _`` 1 ``_ has been removed_.

A subtree of a node `` node `` is `` node `` plus every node that is a descendant of `` node ``.

 

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width: 500px; height: 140px;"/>

```
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```

__Example 2:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width: 500px; height: 115px;"/>

```
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```

__Example 3:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png" style="width: 500px; height: 134px;"/>

```
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 200] ``.
*   `` Node.val `` is either `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 292,817 | 212,735 | 72.7% |