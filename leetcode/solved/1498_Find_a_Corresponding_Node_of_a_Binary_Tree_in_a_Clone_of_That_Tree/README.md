### [1498. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)

Easy

Given two binary trees `` original `` and `` cloned `` and given a reference to a node `` target `` in the original tree.

The `` cloned `` tree is a __copy of__ the `` original `` tree.

Return _a reference to the same node_ in the `` cloned `` tree.

__Note__ that you are __not allowed__ to change any of the two trees or the `` target `` node and the answer __must be__ a reference to a node in the `` cloned `` tree.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e1.png" style="width: 544px; height: 426px;"/>

```
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e2.png" style="width: 221px; height: 159px;"/>

```
Input: tree = [7], target =  7
Output: 7
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e3.png" style="width: 459px; height: 486px;"/>

```
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
```

 

__Constraints:__

*   The number of nodes in the `` tree `` is in the range <code>[1, 10<sup>4</sup>]</code>.
*   The values of the nodes of the `` tree `` are unique.
*   `` target `` node is a node from the `` original `` tree and is not `` null ``.

 

__Follow up:__ Could you solve the problem if repeated values on the tree are allowed?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 172,176 | 150,696 | 87.5% |