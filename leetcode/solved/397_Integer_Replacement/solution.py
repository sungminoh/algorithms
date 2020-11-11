
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""
from collections import deque
import pytest


class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        queue = deque()
        visited = set()
        visited.add(n)
        queue.append((n, 0))
        while queue:
            num, step = queue.popleft()
            step += 1
            if num % 2 == 0:
                if num // 2 == 1:
                    return step
                if num // 2 not in visited:
                    visited.add(num // 2)
                    queue.append((num // 2, step))
            else:
                if num - 1 == 1 or num + 1 == 1:
                    return step
                if num - 1 not in visited:
                    visited.add(num - 1)
                    queue.append((num - 1, step))
                if num + 1 not in visited:
                    visited.add(num + 1)
                    queue.append((num + 1, step))


@pytest.mark.parametrize('n, expected', [
    (8, 3),
])
def test(n, expected):
    assert expected == Solution().integerReplacement(n)
