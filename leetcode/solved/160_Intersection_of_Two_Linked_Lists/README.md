### [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

Easy

Given the heads of two singly linked-lists `` headA `` and `` headB ``, return _the node at which the two lists intersect_. If the two linked lists have no intersection at all, return `` null ``.

For example, the following two linked lists begin to intersect at node `` c1 ``:

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_statement.png" style="width: 500px; height: 162px;"/>

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

__Note__ that the linked lists must __retain their original structure__ after the function returns.

__Custom Judge:__

The inputs to the __judge__ are given as follows (your program is __not__ given these inputs):

*   `` intersectVal `` - The value of the node where the intersection occurs. This is `` 0 `` if there is no intersected node.
*   `` listA `` - The first linked list.
*   `` listB `` - The second linked list.
*   `` skipA `` - The number of nodes to skip ahead in `` listA `` (starting from the head) to get to the intersected node.
*   `` skipB `` - The number of nodes to skip ahead in `` listB `` (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, `` headA `` and `` headB `` to your program. If you correctly return the intersected node, then your solution will be __accepted__.

 

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" style="width: 500px; height: 162px;"/>

```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
```

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" style="width: 500px; height: 194px;"/>

```
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
```

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png" style="width: 300px; height: 189px;"/>

```
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
```

 

__Constraints:__

*   The number of nodes of `` listA `` is in the `` m ``.
*   The number of nodes of `` listB `` is in the `` n ``.
*   <code>1 <= m, n <= 3 * 10<sup>4</sup></code>
*   <code>1 <= Node.val <= 10<sup>5</sup></code>
*   `` 0 <= skipA < m ``
*   `` 0 <= skipB < n ``
*   `` intersectVal `` is `` 0 `` if `` listA `` and `` listB `` do not intersect.
*   `` intersectVal == listA[skipA] == listB[skipB] `` if `` listA `` and `` listB `` intersect.

 
__Follow up:__ Could you write a solution that runs in `` O(m + n) `` time and use only `` O(1) `` memory?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,975,019 | 1,019,186 | 51.6% |