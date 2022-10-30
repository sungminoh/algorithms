### [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

Easy

Given the `` root `` of a Binary Search Tree and a target number `` k ``, return _`` true `` if there exist two elements in the BST such that their sum is equal to the given target_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="width: 400px; height: 229px;"/>

```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="width: 400px; height: 229px;"/>

```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code>
*   `` root `` is guaranteed to be a __valid__ binary search tree.
*   <code>-10<sup>5</sup> <= k <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 684,429 | 417,232 | 61.0% |