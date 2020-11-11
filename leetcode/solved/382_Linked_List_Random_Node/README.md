### [382. Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/)

Medium

Given a singly linked list, return a random node's value from the linked list. Each node must have the __same probability__ of being chosen.

__Follow up:__  
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

__Example:__

```
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 128,423 | 65,888 | 51.3% |