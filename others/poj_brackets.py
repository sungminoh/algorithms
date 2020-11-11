#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import pytest
from functools import lru_cache


def find_maximum_regular_brackets(s):
    matches = {'[]', '()'}
    @lru_cache()
    def _rec(i, j):
        if i > j-2:
            return 0
        elif i == j-2:
            if s[i:j] in matches:
                return 2
            else:
                return 0
        else:
            m = max(_rec(i, k) + _rec(k, j) for k in range(i+1, j))
            if s[i] + s[j-1] in matches:
                m = max(m, 2 + _rec(i+1, j-1))
        return m
    return _rec(0, len(s))


@pytest.mark.parametrize('s, expected', [
    ('()', 2),
    ('[]', 2),
    ('(())', 4),
    ('()[]', 4),
    ('()[()]', 6),
    ('((()))', 6),
    ('()()()', 6),
    ('()()()', 6),
    ('([]])', 4),
    (')[)(', 0),
    ('([][][)', 6),
])
def test(s, expected):
    assert expected == find_maximum_regular_brackets(s)

