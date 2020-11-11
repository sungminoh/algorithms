#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

	get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
	addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
	addAtTail(val) : Append a node of value val to the last element of the linked list.
	addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
	deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:

Input:
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:
[null,null,null,null,2,null,3]

Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Constraints:

	0 <= index,val <= 1000
	Please do not use the built-in LinkedList library.
	At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.
"""
import sys
import pytest


class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = self.prev = None

        def __repr__(self):
            return f'({self.val!r})'

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.tail = None
        self.size = 0

    def _node(self, index: int) -> 'MyLinkedList.Node':
        if index >= self.size:
            return None
        if index < self.size / 2:
            n = self.root
            move = lambda n: n.next
        else:
            n = self.tail
            index = self.size-1 - index
            move = lambda n: n.prev
        for _ in range(index):
            n = move(n)
        return n

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        n = self._node(index)
        if n:
            return n.val
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.size += 1
        n = self.Node(val)
        if not self.root:
            self.root = self.tail = n
            return
        n.next = self.root
        self.root.prev = n
        self.root = n

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.size += 1
        n = self.Node(val)
        if not self.root:
            self.root = self.tail = n
            return
        n.prev = self.tail
        self.tail.next = n
        self.tail = n


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            n = self._node(index)
            p = n.prev
            new = self.Node(val)
            p.next = new
            new.next = n
            n.prev = new
            new.prev = p
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.root = self.root.next
            if self.root:
                self.root.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            n = self._node(index)
            n.prev.next = n.next
            n.next.prev = n.prev
        self.size -= 1

    def __repr__(self):
        n = self.root
        nodes = []
        while n:
            nodes.append(n)
            n = n.next
        return '->'.join(repr(n) for n in nodes)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        pass


@pytest.mark.parametrize('commands, args, expecteds', [
    (["MyLinkedList","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtHead","get","addAtTail","addAtHead","get","addAtTail","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","get","addAtIndex","addAtHead","get","addAtHead","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","addAtTail","addAtHead","get","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","get","get","addAtHead","addAtTail","addAtTail","addAtTail","addAtIndex","get","addAtHead","addAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","deleteAtIndex","get","get","addAtHead","get","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtTail","addAtTail","get","addAtIndex","addAtHead","deleteAtIndex","addAtTail","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtTail","addAtTail"],
     [[],[38],[66],[61],[76],[26],[37],[8],[5],[4],[45],[4],[85],[37],[5],[93],[10,23],[21],[52],[15],[47],[12],[6,24],[64],[4],[31],[6],[40],[17],[15],[19,2],[11],[86],[17],[55],[15],[14,95],[22],[66],[95],[8],[47],[23],[39],[30],[27],[0],[99],[45],[4],[9,11],[6],[81],[18,32],[20],[13],[42],[37,91],[36],[10,37],[96],[57],[20],[89],[18],[41,5],[23],[75],[7],[25,51],[48],[46],[29],[85],[82],[6],[38],[14],[1],[12],[42],[42],[83],[13],[14,20],[17,34],[36],[58],[2],[38],[33,59],[37],[15],[64],[56],[0],[40],[92],[63],[35],[62],[32]],
     [None,None,None,None,None,None,None,None,None,None,None,61,None,None,61,None,None,None,None,None,None,85,None,None,37,None,None,None,None,None,None,None,None,23,None,None,None,None,None,None,None,None,None,None,-1,95,None,None,None,None,None,31,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,8,None,None,None,None,None,None,None,None,None,6,47,None,23,None,None,None,None,None,None,None,93,None,None,None,None,48,None,93,None,None,59,None,None])
])
def test(commands, args, expecteds):
    o = MyLinkedList(*args[0])
    for c, a, e in zip(commands[1:], args[1:], expecteds[1:]):
        r = getattr(o, c)(*a)
        print(c, a, r)
        assert e == r

if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
