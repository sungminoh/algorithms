### [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

Medium

Given the `` head `` of a singly linked list where elements are sorted in __ascending order__, convert _it to a _<span data-keyword="height-balanced">___height-balanced___</span> _binary search tree_.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/linked.jpg" style="width: 500px; height: 388px;"/>

```
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```

<strong class="example">Example 2:</strong>

```
Input: head = []
Output: []
```

 

__Constraints:__

*   The number of nodes in `` head `` is in the range <code>[0, 2 * 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 784,139 | 472,387 | 60.2% |