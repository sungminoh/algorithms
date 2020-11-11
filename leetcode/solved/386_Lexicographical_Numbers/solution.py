#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
from typing import List
import pytest


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(int, sorted(map(str, list(range(1, n + 1))))))


@pytest.mark.parametrize('n, expected', [
    (13, [1,10,11,12,13,2,3,4,5,6,7,8,9])

])
def test(n, expected):
    assert expected == Solution().lexicalOrder(n)
