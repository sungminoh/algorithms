### [1465. Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)

Medium

Given the `` root `` of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return _the maximum product of the sums of the two subtrees_. Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

__Note__ that you need to maximize the answer before taking the mod and not after taking it.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png" style="width: 500px; height: 167px;"/>

```
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png" style="width: 500px; height: 211px;"/>

```
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
```

__Example 3:__

```
Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
```

__Example 4:__

```
Input: root = [1,1]
Output: 1
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[2, 5 * 10<sup>4</sup>]</code>.
*   <code>1 <= Node.val <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 113,534 | 47,967 | 42.2% |