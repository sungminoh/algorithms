### [652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/)

Medium

Given the `` root `` of a binary tree, return all __duplicate subtrees__.

For each kind of duplicate subtrees, you only need to return the root node of any __one__ of them.

Two trees are __duplicate__ if they have the __same structure__ with the __same node values__.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e1.jpg" style="width: 450px; height: 354px;"/>

```
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e2.jpg" style="width: 321px; height: 201px;"/>

```
Input: root = [2,1,1]
Output: [[1]]
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e33.jpg" style="width: 450px; height: 303px;"/>

```
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
```

 

__Constraints:__

*   The number of the nodes in the tree will be in the range `` [1, 5000] ``
*   `` -200 <= Node.val <= 200 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 388,545 | 229,146 | 59.0% |