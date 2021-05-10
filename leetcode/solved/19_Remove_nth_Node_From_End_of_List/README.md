### [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Medium

Given the `` head `` of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.

__Follow up:__ Could you do this in one pass?

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;"/>

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

__Example 2:__

```
Input: head = [1], n = 1
Output: []
```

__Example 3:__

```
Input: head = [1,2], n = 1
Output: [1]
```

 

__Constraints:__

*   The number of nodes in the list is `` sz ``.
*   `` 1 <= sz <= 30 ``
*   `` 0 <= Node.val <= 100 ``
*   `` 1 <= n <= sz ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,393,809 | 866,878 | 36.2% |