### [1093. Recover a Tree From Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/)

Hard

We run a preorder depth-first search (DFS) on the `` root `` of a binary tree.

At each node in this traversal, we output `` D `` dashes (where `` D `` is the depth of this node), then we output the value of this node.  If the depth of a node is `` D ``, the depth of its immediate child is `` D + 1 ``.  The depth of the `` root `` node is `` 0 ``.

If a node has only one child, that child is guaranteed to be __the left child__.

Given the output `` traversal `` of this traversal, recover the tree and return _its_ `` root ``.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/08/recover-a-tree-from-preorder-traversal.png" style="width: 320px; height: 200px;"/>

```
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114101-pm.png" style="width: 256px; height: 250px;"/>

```
Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114955-pm.png" style="width: 276px; height: 250px;"/>

```
Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
```

 

__Constraints:__

*   The number of nodes in the original tree is in the range `` [1, 1000] ``.
*   <code>1 <= Node.val <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 67,285 | 50,007 | 74.3% |