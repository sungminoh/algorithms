
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []

Constraints:

	0
	num only contain digits.
"""
from functools import reduce
from pprint import pprint
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ret = []
        def dfs(i, exp, cur,  prev):
            if i == len(num) and cur == target:
                ret.append(exp)
                return
            for j in range(i+1, len(num) + 1):
                s = num[i:j]
                if len(s) > 1 and s.startswith('0'):
                    continue
                n = int(s)
                if exp == '':
                    dfs(j, f'{n}', n, n)
                else:
                    dfs(j, f'{exp}+{n}', cur + n, n)
                    dfs(j, f'{exp}-{n}', cur - n, -n)
                    dfs(j, f'{exp}*{n}', cur - prev + (prev * n), (prev * n))
        dfs(0, '', 0, 0)
        return ret

    def _addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        def all_subgroups(lst):
            if len(lst) == 0:
                yield []
            elif len(lst) == 1:
                yield [lst]
            else:
                for i in range(1, len(lst)+1):
                    for sub in all_subgroups(lst[i:]):
                        yield [lst[:i]] + sub

        groups = []
        for group in all_subgroups(num):
            if any(len(x) > 1 and x.startswith('0') for x in group):
                continue
            groups.append(group)
        cases = []
        for group in groups:
            for case in all_subgroups(group):
                cases.append([(reduce(lambda x, y: x*y, map(int,nums)), '*'.join(nums)) for nums in case])

        def _rec(nums, i):
            if i in memo:
                return
            memo[i] = defaultdict(set)
            val, exp = nums[i]
            if i == 0:
                val, exp = nums[i]
                memo[i][val].add(exp)
            else:
                _rec(nums, i-1)
                for v, exps in memo[i-1].items():
                    memo[i][v + val].update({f'{e}+{exp}' for e in exps})
                    memo[i][v - val].update({f'{e}-{exp}' for e in exps})

        ret = []
        for case in cases:
            memo = dict()  # i -> val -> expressions
            _rec(case, len(case)-1)
            ret.extend(memo[len(case)-1][target])
        return ret


@pytest.mark.parametrize('num, target, expected', [
    ("123", 6, ["1+2+3", "1*2*3"]),
    ("232", 8, ["2*3+2", "2+3*2"]),
    ("105", 5, ["1*0+5","10-5"]),
    ("00", 0, ["0+0", "0-0", "0*0"]),
    ("3456237490", 9191, []),
    ("123456789", 45, ["1*2*3*4*5-6-78+9","1*2*3*4+5+6-7+8+9","1*2*3+4+5+6+7+8+9","1*2*3+4+5-6*7+8*9","1*2*3+4-5*6+7*8+9","1*2*3+4-5*6-7+8*9","1*2*3-4*5+6*7+8+9","1*2*3-4*5-6+7*8+9","1*2*3-4*5-6-7+8*9","1*2*3-45+67+8+9","1*2*34+56-7-8*9","1*2*34-5+6-7-8-9","1*2+3*4-56+78+9","1*2+3+4+5*6+7+8-9","1*2+3+4-5+6*7+8-9","1*2+3+4-5-6+7*8-9","1*2+3+45+67-8*9","1*2+3-45+6+7+8*9","1*2+34+5-6-7+8+9","1*2+34+56-7*8+9","1*2+34-5+6+7-8+9","1*2+34-56+7*8+9","1*2+34-56-7+8*9","1*2-3*4+5+67-8-9","1*2-3+4-5-6*7+89","1*2-3-4*5+67+8-9","1*2-3-4+56-7-8+9","1*2-34+5*6+7*8-9","1*23+4*5-6+7-8+9","1*23-4-56-7+89","1+2*3*4*5+6+7-89","1+2*3*4+5*6+7-8-9","1+2*3*4-5+6*7-8-9","1+2*3+4*5*6+7-89","1+2*3+4*5-6+7+8+9","1+2*3-4-5-6*7+89","1+2*34-5*6+7+8-9","1+2+3*4*5+6-7-8-9","1+2+3*4+5+6*7-8-9","1+2+3*45-6-78-9","1+2+3+4+5+6+7+8+9","1+2+3+4+5-6*7+8*9","1+2+3+4-5*6+7*8+9","1+2+3+4-5*6-7+8*9","1+2+3-4*5+6*7+8+9","1+2+3-4*5-6+7*8+9","1+2+3-4*5-6-7+8*9","1+2+3-45+67+8+9","1+2-3*4*5+6+7+89","1+2-3*4+5*6+7+8+9","1+2-3*4-5+6*7+8+9","1+2-3*4-5-6+7*8+9","1+2-3*4-5-6-7+8*9","1+2-3+4*5+6*7-8-9","1+2-3+45+6-7-8+9","1+2-3+45-6+7+8-9","1+2-3-4-5*6+7+8*9","1+2-3-45-6+7+89","1+2-34+5+6+7*8+9","1+2-34+5+6-7+8*9","1+2-34-5-6+78+9","1+23*4+5-6-7*8+9","1+23*4-5-6*7+8-9","1+23*4-56+7-8+9","1+23+4+5+6+7+8-9","1+23+4-5*6+7*8-9","1+23+4-5-67+89","1+23-4*5+6*7+8-9","1+23-4*5-6+7*8-9","1+23-4-5+6+7+8+9","1+23-4-5-6*7+8*9","1+23-45+67+8-9","1-2*3*4+5-6+78-9","1-2*3*4-5-6+7+8*9","1-2*3+4*5+6+7+8+9","1-2*3+4*5-6*7+8*9","1-2*3+4+5+6*7+8-9","1-2*3+4+5-6+7*8-9","1-2*3+4+56+7-8-9","1-2*3+45-67+8*9","1-2*3-4+5*6+7+8+9","1-2*3-4-5+6*7+8+9","1-2*3-4-5-6+7*8+9","1-2*3-4-5-6-7+8*9","1-2*34+5*6-7+89","1-2+3*4*5-6-7+8-9","1-2+3+4-5*6+78-9","1-2+3+45+6-7+8-9","1-2+3-4*5-6+78-9","1-2+3-45+6-7+89","1-2-3*4+5+6+7*8-9","1-2-3*4-5-6+78-9","1-2-3+4-5+67-8-9","1-2-3+45-6-7+8+9","1-2-34+5+6+78-9","1-2-34+56+7+8+9","1-2-34-5+6+7+8*9","1-23*4+5+6*7+89","1-23+4*5-6*7+89","1-23+4-5+67-8+9","1-23+45-67+89","1-23-4+5+67+8-9","1-23-4-5-6-7+89","12*3*4-5*6-78+9","12*3+4+5+6-7-8+9","12*3+4+5-6+7+8-9","12*3-4-5-6+7+8+9","12*3-4-56+78-9","12+3*4+5+6-7+8+9","12+3*45-6-7-89","12+3+4-56-7+89","12+3-4*5+67-8-9","12+3-45+6+78-9","12+34-5-6-7+8+9","12-3*4*5+6+78+9","12-3*4-5+67-8-9","12-3+4*5+6-7+8+9","12-3+4+56-7-8-9","12-3-4+5*6-7+8+9","12-3-4-56+7+89","12-3-45-6+78+9"]),
    ("", 5, [])
])
def test(num, target, expected):
    actual = set(Solution().addOperators(num, target))
    for exp in actual:
        assert target == eval(exp)
    assert set(expected) == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
