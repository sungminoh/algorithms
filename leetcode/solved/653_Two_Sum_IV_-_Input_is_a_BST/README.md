### [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

Easy

Given the `` root `` of a Binary Search Tree and a target number `` k ``, return _`` true `` if there exist two elements in the BST such that their sum is equal to the given target_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="width: 562px; height: 322px;"/>

```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="width: 562px; height: 322px;"/>

```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

__Example 3:__

```
Input: root = [2,1,3], k = 4
Output: true
```

__Example 4:__

```
Input: root = [2,1,3], k = 1
Output: false
```

__Example 5:__

```
Input: root = [2,1,3], k = 3
Output: true
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code>
*   `` root `` is guaranteed to be a __valid__ binary search tree.
*   <code>-10<sup>5</sup> <= k <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 415,365 | 239,136 | 57.6% |