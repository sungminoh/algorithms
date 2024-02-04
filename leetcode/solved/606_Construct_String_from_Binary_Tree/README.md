### [606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/description/?envType=daily-question&envId=2023-12-08)

Medium

Given the `` root `` node of a binary tree, your task is to create a string representation of the tree following a specific set of formatting rules. The representation should be based on a preorder traversal of the binary tree and must adhere to the following guidelines:

*   
    
    __Node Representation__: Each node in the tree should be represented by its integer value.
    
    
*   
    
    __Parentheses for Children__: If a node has at least one child (either left or right), its children should be represented inside parentheses. Specifically:
    
    
    
    *   If a node has a left child, the value of the left child should be enclosed in parentheses immediately following the node's value.
    *   If a node has a right child, the value of the right child should also be enclosed in parentheses. The parentheses for the right child should follow those of the left child.
    
    
    
*   
    
    __Omitting Empty Parentheses__: Any empty parentheses pairs (i.e., `` () ``) should be omitted from the final string representation of the tree, with one specific exception: when a node has a right child but no left child. In such cases, you must include an empty pair of parentheses to indicate the absence of the left child. This ensures that the one-to-one mapping between the string representation and the original binary tree structure is maintained.
    
    
    
    In summary, empty parentheses pairs should be omitted when a node has only a left child or no children. However, when a node has a right child but no left child, an empty pair of parentheses must precede the representation of the right child to reflect the tree's structure accurately.
    
    

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg" style="padding: 10px; background: #fff; border-radius: .5rem;"/>

```
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the empty parenthesis pairs. And it will be "1(2(4))(3)".
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg" style="padding: 10px; background: #fff; border-radius: .5rem;"/>

<strong>Input:</strong> root = [1,2,3,null,4]
    <strong>Output:</strong> "1(2()(4))(3)"
    <strong>Explanation:</strong> Almost the same as the first example, except the () after <code>2</code> is necessary to indicate the absence of a left child for <code>2</code> and the presence of a right child.

 

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   `` -1000 <= Node.val <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 449,919 | 310,356 | 69.0% |