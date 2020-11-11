### [623. Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree/)

Medium

Given the root of a binary tree, then value `` v `` and depth `` d ``, you need to add a row of nodes with value `` v `` at the given depth `` d ``. The root node is at depth 1. 

The adding rule is: given a positive integer depth `` d ``, for each NOT null tree nodes `` N `` in depth `` d-1 ``, create two tree nodes with value `` v `` as `` N's `` left subtree root and right subtree root. And `` N's `` __original left subtree__ should be the left subtree of the new left subtree root, its __original right subtree__ should be the right subtree of the new right subtree root. If depth `` d `` is 1 that means there is no depth d-1 at all, then create a tree node with value __v__ as the new root of the whole original tree, and the original tree is the new root's left subtree.

__Example 1:__  

```
<b>Input:</b> 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

<b>v = 1</b>

<b>d = 2</b>

<b>Output:</b> 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

```

__Example 2:__  

```
<b>Input:</b> 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

<b>v = 1</b>

<b>d = 3</b>

<b>Output:</b> 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
```

__Note:__  

1.   The given d is in range \[1, maximum depth of the given tree + 1\].
2.   The given binary tree has at least one tree node.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 74,394 | 36,669 | 49.3% |