### [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

Easy

Given the `` head `` of a linked list and an integer `` val ``, remove all the nodes of the linked list that has `` Node.val == val ``, and return _the new head_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;"/>

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

__Example 2:__

```
Input: head = [], val = 1
Output: []
```

__Example 3:__

```
Input: head = [7,7,7,7], val = 7
Output: []
```

 

__Constraints:__

*   The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   `` 1 <= Node.val <= 50 ``
*   `` 0 <= val <= 50 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,403,194 | 590,144 | 42.1% |