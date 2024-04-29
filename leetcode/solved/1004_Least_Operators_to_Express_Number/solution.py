#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

	The division operator (/) returns rational numbers.
	There are no parentheses placed anywhere.
	We use the usual order of operations: multiplication and division happen before addition and subtraction.
	It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.

We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.

Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.
The expression contains 5 operations.

Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
The expression contains 8 operations.

Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.
The expression contains 3 operations.

Constraints:

	2 <= x <= 100
	1 <= target <= 2 * 108
"""
from collections import deque
import pytest
import sys


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """Apr 28, 2024 15:39 TLE"""
        ret = 0
        queue = deque([str(x)])
        while queue:
            for _ in range(len(queue)):
                eq = queue.popleft()
                if eval(eq) == target:
                    return ret
                for op in '*/+-':
                    queue.append(f'{eq}{op}{x}')
            ret += 1
        return -1

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """Wrong"""
        ret = 0
        seen = set()
        queue = deque([(x, target)])
        while queue:
            for _ in range(len(queue)):
                cur, tar = queue.popleft()
                if cur == tar:
                    return ret
                for nxt in [
                    (cur*x, tar),
                    (cur, tar*x),
                    (cur+x, tar),
                    (cur, tar+x),
                ]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            ret += 1
        return -1

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """Apr 28, 2024 16:34"""
        positive = negative = 0
        p = 0
        while target:
            target, remain = divmod(target, x)
            if p > 0:
                positive, negative = min(
                    positive + remain * p,
                    negative + (remain+1) * p,
                ), min(
                    positive + (x-remain) * p,
                    negative + (x-1-remain) * p,
                )
            else:
                positive, negative = remain * 2, (x-remain) * 2
            p += 1
        return min(positive, p+negative)-1


@pytest.mark.parametrize('args', [
    ((3, 19, 5)),
    ((5, 501, 8)),
    ((100, 100000000, 3)),
    ((3, 365, 17)),
])
def test(args):
    assert args[-1] == Solution().leastOpsExpressTarget(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
