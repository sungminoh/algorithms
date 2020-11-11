### [655. Print Binary Tree](https://leetcode.com/problems/print-binary-tree/)

Medium

Print a binary tree in an m\*n 2D string array following these rules: 

1.   The row number `` m `` should be equal to the height of the given binary tree.
2.   The column number `` n `` should always be an odd number.
3.   The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (__left-bottom part and right-bottom part__). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them. 
4.   Each unused space should contain an empty string `` "" ``.
5.   Print the subtrees following the same rules.

__Example 1:__  

```
<b>Input:</b>
     1
    /
   2
<b>Output:</b>
[["", "1", ""],
 ["2", "", ""]]
```

__Example 2:__  

```
<b>Input:</b>
     1
    / \
   2   3
    \
     4
<b>Output:</b>
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
```

__Example 3:__  

```
<b>Input:</b>
      1
     / \
    2   5
   / 
  3 
 / 
4 
<b>Output:</b>

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
```

__Note:__The height of binary tree is in the range of \[1, 10\].

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 58,471 | 32,023 | 54.8% |