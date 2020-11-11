### [764. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

Medium

Given an n-ary tree, return the _level order_ traversal of its nodes' values.

_Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples)._

 

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;"/>

```
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [[1],[3,2,4],[5,6]]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;"/>

```
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

 

__Constraints:__

*   The height of the n-ary tree is less than or equal to `` 1000 ``
*   The total number of nodes is between `` [0, 10^4] ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 104,650 | 66,314 | 63.4% |