### [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

Medium

You are given two __non-empty__ linked lists representing two non-negative integers. The digits are stored in __reverse order__, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;"/>

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

__Example 2:__

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

__Example 3:__

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

 

__Constraints:__

*   The number of nodes in each linked list is in the range `` [1, 100] ``.
*   `` 0 <= Node.val <= 9 ``
*   It is guaranteed that the list represents a number that does not have leading zeros.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 6,876,009 | 2,638,494 | 38.4% |