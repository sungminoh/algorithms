### [776. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)

Easy

Given the `` root `` of an n-ary tree, return _the postorder traversal of its nodes' values_.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;"/>

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;"/>

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>0 <= Node.val <= 10<sup>4</sup></code>
*   The height of the n-ary tree is less than or equal to `` 1000 ``.

 

__Follow up:__ Recursive solution is trivial, could you do it iteratively?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 177,646 | 131,137 | 73.8% |