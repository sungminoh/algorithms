### [1568. Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24)

Medium

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be __pseudo-palindromic__ if at least one permutation of the node values in the path is a palindrome.

_Return the number of __pseudo-palindromic__ paths going from the root node to leaf nodes._

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/05/06/palindromic_paths_1.png" style="width: 300px; height: 201px;"/>

```
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

<strong class="example">Example 2:</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/05/07/palindromic_paths_2.png" style="width: 300px; height: 314px;"/></strong>

```
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

<strong class="example">Example 3:</strong>

```
Input: root = [9]
Output: 1
```

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.
*   `` 1 <= Node.val <= 9 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 307,639 | 210,778 | 68.5% |