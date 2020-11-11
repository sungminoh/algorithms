#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
from typing import List
from heapq import heappop, heappush


class Heap():
    def __init__(self, key_func=lambda x, y: x == y):
        self.h = []
        self.key_func = key_func

    def pop(self):
        ret = []
        head = self.h[0]
        while self.h and self.h[0][0] == head[0]:
            ret.append(heappop(self.h)[1])
        return ret

    def push(self, v):
        heappush(self.h, (self.key_func(v), v))

    def peak(self):
        return self.h[0][1]


class LinkedList():
    class Node():
        def __init__(self, val):
            self.val = val
            self.next = None

        def __repr__(self):
            return 'Node(%s)' % self.val

    def __init__(self):
        self.head = self.tail = None

    def append(self, val):
        if not self.head:
            self.head = self.tail = self.Node(val)
        else:
            node = self.Node(val)
            self.tail.next = node
            self.tail = node

    def clean_up_until(self, val):
        while self.head.val < val:
            self.head = self.head.next

    def __repr__(self):
        reps = []
        node = self.head
        while node:
            reps.append(node.__repr__())
            node = node.next
        return '->'.join(reps)


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primes = list(sorted(primes))
        queue = LinkedList()
        queue.append(1)
        m = 1
        # setup heap
        heap = Heap(key_func=lambda x: x[0] * x[1].val)
        for p in primes:
            heap.push((p, queue.tail))
        print('initial heap: ', heap.h)
        print('initial queue: ', queue)
        while m < n:
            mins = heap.pop()
            print('mins:', mins)
            p, node = mins[0]
            queue.append(node.val * p)
            print('queue: ', queue)
            m += 1
            for p, node in mins:
                heap.push((p, node.next))
            queue.clean_up_until(heap.peak()[1].val)

        return queue.tail.val


if __name__ == '__main__':
    cases = [
        ((12, [2,7,13,19]), 32),
        ((2, [2]), 2)
    ]
    for case, expected in cases:
        actual = Solution().nthSuperUglyNumber(*case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
