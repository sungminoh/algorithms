### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

Easy

Given `` head ``, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `` next `` pointer. Internally, `` pos `` is used to denote the index of the node that tail's `` next `` pointer is connected to. __Note that `` pos `` is not passed as a parameter__.

Return `` true ``_ if there is a cycle in the linked list_. Otherwise, return `` false ``.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="width: 300px; height: 97px; margin-top: 8px; margin-bottom: 8px;"/>

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="width: 141px; height: 74px;"/>

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="width: 45px; height: 45px;"/>

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

 

__Constraints:__

*   The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>
*   `` pos `` is `` -1 `` or a __valid index__ in the linked-list.

 

__Follow up:__ Can you solve it using `` O(1) `` (i.e. constant) memory?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,984,542 | 1,362,859 | 45.7% |