### [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Medium

Given the `` head `` of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;"/>

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

<strong class="example">Example 2:</strong>

```
Input: head = [1], n = 1
Output: []
```

<strong class="example">Example 3:</strong>

```
Input: head = [1,2], n = 1
Output: [1]
```

 

__Constraints:__

*   The number of nodes in the list is `` sz ``.
*   `` 1 <= sz <= 30 ``
*   `` 0 <= Node.val <= 100 ``
*   `` 1 <= n <= sz ``

 

__Follow up:__ Could you do this in one pass?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 4,366,868 | 1,741,206 | 39.9% |