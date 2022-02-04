### [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

Medium

Given the `` head `` of a linked list, return _the node where the cycle begins. If there is no cycle, return _`` null ``.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `` next `` pointer. Internally, `` pos `` is used to denote the index of the node that tail's `` next `` pointer is connected to (__0-indexed__). It is `` -1 `` if there is no cycle. __Note that__ `` pos `` __is not passed as a parameter__.

__Do not modify__ the linked list.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="height: 145px; width: 450px;"/>

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 105px; width: 201px;"/>

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 65px; width: 65px;"/>

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

 

__Constraints:__

*   The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>
*   `` pos `` is `` -1 `` or a __valid index__ in the linked-list.

 

__Follow up:__ Can you solve it using `` O(1) `` (i.e. constant) memory?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,404,095 | 611,060 | 43.5% |