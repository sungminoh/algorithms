### [904. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)

Easy

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a __leaf value sequence___._

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="width: 400px; height: 336px;"/>

For example, in the given tree above, the leaf value sequence is `` (6, 7, 4, 9, 8) ``.

Two binary trees are considered _leaf-similar_ if their leaf value sequence is the same.

Return `` true `` if and only if the two given trees with head nodes `` root1 `` and `` root2 `` are leaf-similar.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg" style="width: 600px; height: 237px;"/>

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg" style="width: 300px; height: 110px;"/>

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

 

__Constraints:__

*   The number of nodes in each tree will be in the range `` [1, 200] ``.
*   Both of the given trees will have values in the range `` [0, 200] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 367,559 | 248,551 | 67.6% |