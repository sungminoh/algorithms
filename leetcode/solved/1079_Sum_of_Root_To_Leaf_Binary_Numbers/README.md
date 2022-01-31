### [1079. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)

Easy

You are given the `` root `` of a binary tree where each node has a value `` 0 `` or `` 1 ``. Each root-to-leaf path represents a binary number starting with the most significant bit.

*   For example, if the path is `` 0 -> 1 -> 1 -> 0 -> 1 ``, then this could represent `` 01101 `` in binary, which is `` 13 ``.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return _the sum of these numbers_.

The test cases are generated so that the answer fits in a __32-bits__ integer.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png" style="width: 400px; height: 263px;"/>

```
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

__Example 2:__

```
Input: root = [0]
Output: 0
```

 

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 1000] ``.
*   `` Node.val `` is `` 0 `` or `` 1 ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 205,573 | 151,948 | 73.9% |