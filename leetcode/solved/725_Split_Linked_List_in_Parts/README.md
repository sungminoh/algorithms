### [725. Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)

Medium

Given a (singly) linked list with head node `` root ``, write a function to split the linked list into `` k `` consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.



Examples
1->2->3->4, k = 5 // 5 equal parts
[ [1], 
[2],
[3],
[4],
null ]


__Example 1:__  

<pre style="white-space: pre-line">
<b>Input:</b> 
root = [1, 2, 3], k = 5
<b>Output:</b> [[1],[2],[3],[],[]]
<b>Explanation:</b>
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
```

__Example 2:__  

```
<b>Input:</b> 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
<b>Output:</b> [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
<b>Explanation:</b>
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```

__Note:__<li>The length of <code>root</code> will be in the range <code>[0, 1000]</code>.</li><li>Each value of a node in the input will be an integer in the range <code>[0, 999]</code>.</li><li><code>k</code> will be an integer in the range <code>[1, 50]</code>.</li>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 97,161 | 50,868 | 52.4% |