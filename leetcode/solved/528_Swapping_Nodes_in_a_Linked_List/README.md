### [528. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)

Medium

You are given the `` head `` of a linked list, and an integer `` k ``.

Return _the head of the linked list after __swapping__ the values of the _<code>k<sup>th</sup></code> _node from the beginning and the _<code>k<sup>th</sup></code> _node from the end (the list is __1-indexed__)._

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg" style="width: 400px; height: 112px;"/>

```
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

__Example 2:__

```
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
```

 

__Constraints:__

*   The number of nodes in the list is `` n ``.
*   <code>1 <= k <= n <= 10<sup>5</sup></code>
*   `` 0 <= Node.val <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 230,307 | 157,575 | 68.4% |