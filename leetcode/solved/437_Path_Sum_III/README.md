### [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

Medium

Given the `` root `` of a binary tree and an integer `` targetSum ``, return _the number of paths where the sum of the values along the path equals_ `` targetSum ``.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg" style="width: 450px; height: 386px;"/>

```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
```

__Example 2:__

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 1000] ``.
*   <code>-10<sup>9</sup> <= Node.val <= 10<sup>9</sup></code>
*   `` -1000 <= targetSum <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 646,858 | 320,914 | 49.6% |