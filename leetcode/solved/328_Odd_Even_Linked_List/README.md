### [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

Medium

Given the `` head `` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return _the reordered list_.

The __first__ node is considered __odd__, and the __second__ node is __even__, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `` O(1) `` extra space complexity and `` O(n) `` time complexity.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg" style="width: 300px; height: 123px;"/>

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg" style="width: 500px; height: 142px;"/>

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

 

__Constraints:__

*   `` n ==  ``number of nodes in the linked list
*   <code>0 <= n <= 10<sup>4</sup></code>
*   <code>-10<sup>6</sup> <= Node.val <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 800,893 | 472,474 | 59.0% |