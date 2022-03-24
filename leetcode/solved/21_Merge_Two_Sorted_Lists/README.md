### [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Easy

You are given the heads of two sorted linked lists `` list1 `` and `` list2 ``.

Merge the two lists in a one __sorted__ list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;"/>

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

__Example 2:__

```
Input: list1 = [], list2 = []
Output: []
```

__Example 3:__

```
Input: list1 = [], list2 = [0]
Output: [0]
```

 

__Constraints:__

*   The number of nodes in both lists is in the range `` [0, 50] ``.
*   `` -100 <= Node.val <= 100 ``
*   Both `` list1 `` and `` list2 `` are sorted in __non-decreasing__ order.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 3,445,495 | 2,066,996 | 60.0% |