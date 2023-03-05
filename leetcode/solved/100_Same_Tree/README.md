### [100. Same Tree](https://leetcode.com/problems/same-tree/)

Easy

Given the roots of two binary trees `` p `` and `` q ``, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg" style="width: 622px; height: 182px;"/>

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg" style="width: 382px; height: 182px;"/>

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg" style="width: 622px; height: 182px;"/>

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

 

__Constraints:__

*   The number of nodes in both trees is in the range `` [0, 100] ``.
*   <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,519,851 | 1,461,502 | 58.0% |