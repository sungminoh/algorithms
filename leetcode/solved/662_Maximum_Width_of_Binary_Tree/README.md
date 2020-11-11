### [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)

Medium

Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the `` null `` nodes between the end-nodes are also counted into the length calculation.

It is __guaranteed__ that the answer will in the range of 32-bit signed integer.

__Example 1:__

```
<b>Input:</b> 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

<b>Output:</b> 4
<b>Explanation:</b> The maximum width existing in the third level with the length 4 (5,3,null,9).
```

__Example 2:__

```
<b>Input:</b> 

          1
         /  
        3    
       / \       
      5   3     

<b>Output:</b> 2
<b>Explanation:</b> The maximum width existing in the third level with the length 2 (5,3).
```

__Example 3:__

```
<b>Input:</b> 

          1
         / \
        3   2 
       /        
      5      

<b>Output:</b> 2
<b>Explanation:</b> The maximum width existing in the second level with the length 2 (3,2).
```

__Example 4:__

```
<b>Input:</b> 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
<b>Output:</b> 8
<b>Explanation:</b>The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```

 

__Constraints:__

*   The given binary tree will have between `` 1 `` and `` 3000 `` nodes.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 220,550 | 90,673 | 41.1% |