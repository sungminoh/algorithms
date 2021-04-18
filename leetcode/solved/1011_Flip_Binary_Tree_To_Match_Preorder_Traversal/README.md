### [1011. Flip Binary Tree To Match Preorder Traversal](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/)

Medium

You are given the `` root `` of a binary tree with `` n `` nodes, where each node is uniquely assigned a value from `` 1 `` to `` n ``. You are also given a sequence of `` n `` values `` voyage ``, which is the __desired__ <a href="https://en.wikipedia.org/wiki/Tree_traversal#Pre-order" target="_blank">__pre-order traversal__</a> of the binary tree.

Any node in the binary tree can be __flipped__ by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg" style="width: 400px; height: 187px;"/>

Flip the __smallest__ number of nodes so that the __pre-order traversal__ of the tree __matches__ `` voyage ``.

Return _a list of the values of all __flipped__ nodes. You may return the answer in __any order__. If it is __impossible__ to flip the nodes in the tree to make the pre-order traversal match _`` voyage ``_, return the list _`` [-1] ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-01.png" style="width: 150px; height: 205px;"/>

```
Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 150px; height: 142px;"/>

```
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 150px; height: 142px;"/>

```
Input: root = [1,2,3], voyage = [1,2,3]
Output: []
Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.
```

 

__Constraints:__

*   The number of nodes in the tree is `` n ``.
*   `` n == voyage.length ``
*   `` 1 <= n <= 100 ``
*   `` 1 <= Node.val, voyage[i] <= n ``
*   All the values in the tree are __unique__.
*   All the values in `` voyage `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 59,594 | 29,856 | 50.1% |