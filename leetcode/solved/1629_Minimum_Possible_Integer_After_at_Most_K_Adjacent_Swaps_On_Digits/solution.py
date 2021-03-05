#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string num representing the digits of a very large integer and an integer k.

You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.

Example 1:

Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.

Example 2:

Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.

Example 3:

Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.

Example 4:

Input: num = "22", k = 22
Output: "22"

Example 5:

Input: num = "9438957234785635408", k = 23
Output: "0345989723478563548"

Constraints:

	1 <= num.length <= 30000
	num contains digits only and doesn't have leading zeros.
	1 <= k <= 10^9
"""
from collections import namedtuple
from collections import deque
from collections import defaultdict
from typing import Callable
from typing import Any
from typing import List
import json
import sys
import pytest


Digit = namedtuple('Digit', ['index', 'moves'])

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        remain_num = [(i, ord(x) - ord('0')) for i, x in enumerate(num)][::-1]
        digits = [deque() for _ in range(10)]
        count = 0   # Number of elements in digits
        output = []
        for _ in range(n):
            # Ensure digits has (k + 1) elements (unless insufficient)
            while remain_num and count < k + 1:
                index, x = remain_num.pop()
                # moves: Number of elements before x that are greater than x
                moves = sum(map(len, digits[x+1:]))
                digits[x].append(Digit(index, moves))
                count += 1
            while count > k + 1:
                # Find digit with maximum index
                d = max((digit[-1], i) for i, digit in enumerate(digits) if digit)[1]
                x = digits[d].pop()
                remain_num.append((x.index, d))
                count -= 1
            # Find the minimum element in the list
            d = min(i for i, digit in enumerate(digits) if digit)
            x = digits[d].popleft()
            count -= 1
            k -= x.moves
            output.append(d)
        return ''.join(chr(ord('0') + d) for d in output)


class DigitQueue:
    def __init__(self, n):
        self.size = n
        self.cnt = 0
        self.queues = [deque() for _ in range(10)]

    @property
    def full(self):
        return self.cnt >= self.size

    @property
    def overflow(self):
        return self.cnt > self.size

    def push(self, val, digit):
        self.queues[digit].append((val, sum(len(q) for q in self.queues[digit+1:])))
        self.cnt += 1

    def pop(self):
        digit = max([(q[-1], d) for d, q in enumerate(self.queues) if q])[1]
        self.cnt -= 1
        return digit, self.queues[digit].pop()

    def resize(self, n):
        self.size = n

    def get_next(self):
        digit, queue = min((d, q) for d, q in enumerate(self.queues) if q)
        self.cnt -= 1
        return digit, queue.popleft()


class Solution:
    # O(n*logn)
    def minInteger(self, num: str, k: int) -> str:
        num = list(map(int, num))
        stack = [(i, int(n)) for i, n in enumerate(num)][::-1]
        ret = ''
        queue = DigitQueue(k+1)
        for i in range(len(num)):
            while stack and not queue.full:
                queue.push(*stack.pop())
            while queue.overflow:
                digit, (idx, moves) = queue.pop()
                stack.append((idx, digit))
            digit, (idx, moves) = queue.get_next()
            ret += str(digit)
            queue.resize(queue.size - moves)

        return ret

    # O(n*k)
    def _minInteger(self, num: str, k: int) -> str:
        ret = list(num)
        for i in range(len(num)-1):
            n, j = min([(x, j) for j, x in enumerate(ret[i+1:min(len(ret), i+k+1)], i+1)])
            if n >= ret[i]:
                continue
            ret.insert(i, ret.pop(j))
            k -= j-i
            if k <= 0:
                break
        return ''.join(ret)


@pytest.mark.parametrize('num, k, expected', [
    ("4321", 4, "1342"),
    ("100", 1, "010"),
    ("36789", 1000, "36789"),
    ("22", 22, "22"),
    ("9438957234785635408", 23, "0345989723478563548"),
    ("9000900", 3, "0009900"),
    ("294984148179", 11, "124498948179"),
    ("858957035719081", 2, "588597035719081"),
    # json.loads(open('./testcase.json', 'r').read()),
])
def test(num, k, expected):
    print()
    assert expected == Solution().minInteger(num, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
