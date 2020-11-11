### [835. Linked List Components](https://leetcode.com/problems/linked-list-components/)

Medium

We are given `` head ``, the head node of a linked list containing __unique integer values__.

We are also given the list `` G ``, a subset of the values in the linked list.

Return the number of connected components in `` G ``, where two values are connected if they appear consecutively in the linked list.

__Example 1:__

```
Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
```

__Example 2:__

```
Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
```

__Note: __

*   If `` N `` is the length of the linked list given by `` head ``, `` 1 <= N <= 10000 ``.
*   The value of each node in the linked list will be in the range``  [0, N - 1] ``.
*   `` 1 <= G.length <= 10000 ``.
*   `` G `` is a subset of all values in the linked list.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 71,675 | 40,795 | 56.9% |