### [2216. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

Medium

You are given the `` head `` of a linked list. __Delete__ the __middle node__, and return _the_ `` head `` _of the modified linked list_.

The __middle node__ of a linked list of size `` n `` is the <code>⌊n / 2⌋<sup>th</sup></code> node from the __start__ using __0-based indexing__, where `` ⌊x⌋ `` denotes the largest integer less than or equal to `` x ``.

*   For `` n `` = `` 1 ``, `` 2 ``, `` 3 ``, `` 4 ``, and `` 5 ``, the middle nodes are `` 0 ``, `` 1 ``, `` 1 ``, `` 2 ``, and `` 2 ``, respectively.

 

<strong class="example">Example 1:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg1drawio.png" style="width: 500px; height: 77px;"/>

```
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
```

<strong class="example">Example 2:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg2drawio.png" style="width: 250px; height: 43px;"/>

```
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
```

<strong class="example">Example 3:</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg3drawio.png" style="width: 150px; height: 58px;"/>

```
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
```

 

__Constraints:__

*   The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.
*   <code>1 <= Node.val <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 253,896 | 153,892 | 60.6% |