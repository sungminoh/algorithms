### [1092. Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/)

Medium

Given the `` root `` of a binary tree, find the maximum value `` v `` for which there exist __different__ nodes `` a `` and `` b `` where `` v = |a.val - b.val| `` and `` a `` is an ancestor of `` b ``.

A node `` a `` is an ancestor of `` b `` if either: any child of `` a `` is equal to `` b `` or any child of `` a `` is an ancestor of `` b ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg" style="width: 400px; height: 390px;"/>

```
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg" style="width: 250px; height: 349px;"/>

```
Input: root = [1,null,2,null,0,3]
Output: 3
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [2, 5000] ``.
*   <code>0 <= Node.val <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 262,844 | 199,168 | 75.8% |