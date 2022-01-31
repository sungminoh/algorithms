### [784. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

Medium

You are given the `` root `` node of a binary search tree (BST) and a `` value `` to insert into the tree. Return _the root node of the BST after the insertion_. It is __guaranteed__ that the new value does not exist in the original BST.

__Notice__ that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return __any of them__.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg" style="width: 752px; height: 221px;"/>

```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/bst.jpg" style="width: 352px; height: 301px;"/>
```

__Example 2:__

```
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

__Example 3:__

```
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
```

 

__Constraints:__

*   The number of nodes in the tree will be in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>8</sup> <= Node.val <= 10<sup>8</sup></code>
*   All the values `` Node.val `` are __unique__.
*   <code>-10<sup>8</sup> <= val <= 10<sup>8</sup></code>
*   It's __guaranteed__ that `` val `` does not exist in the original BST.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 365,273 | 274,037 | 75.0% |