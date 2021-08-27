### [1544. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

Medium

Given a binary tree `` root ``, a node _X_ in the tree is named __good__ if in the path from root to _X_ there are no nodes with a value _greater than_ X.

Return the number of __good__ nodes in the binary tree.

 

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png" style="width: 263px; height: 156px;"/></strong>

```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png" style="width: 157px; height: 161px;"/></strong>

```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

__Example 3:__

```
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
```

 

__Constraints:__

*   The number of nodes in the binary tree is in the range `` [1, 10^5] ``.
*   Each node's value is between `` [-10^4, 10^4] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 147,848 | 107,778 | 72.9% |