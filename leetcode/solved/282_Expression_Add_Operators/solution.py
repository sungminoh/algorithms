#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Explanation: Both "1*0+5" and "10-5" evaluate to 5.
Note that "1-05" is not a valid expression because the 5 has a leading zero.

Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Explanation: "0*0", "0+0", and "0-0" all evaluate to 0.
Note that "00" is not a valid expression because the 0 has a leading zero.

Example 5:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

Constraints:

	1 <= num.length <= 10
	num consists of only digits.
	-231 <= target <= 231 - 1
"""
import sys
from functools import lru_cache
from typing import Tuple
from typing import List
import pytest


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """06/16/2020 18:37"""
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

    def addOperators(self, num: str, target: int) -> List[str]:
        """06/16/2020 21:45"""
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

    def addOperators(self, num: str, target: int) -> List[str]:
        @lru_cache(None)
        def dfs(i) -> List[Tuple[int, int, str]]:
            """evaluation, the first term, expression"""
            ret = []
            for j in range(i+1, len(num)):
                h = int(num[i:j])
                if num[i] != '0' or j-i == 1:
                    for v, f, e in dfs(j):
                        ret.append((h+v, h, f'{h}+{e}'))
                        ret.append((h-f+(v-f), h, f'{h}-{e}'))
                        ret.append((h*f+(v-f), h*f, f'{h}*{e}'))
            if num[i] != '0' or i == len(num)-1:
                ret.append((int(num[i:]), int(num[i:]), num[i:]))
            return ret

        return [e for v, f, e in dfs(0) if v == target]


@pytest.mark.parametrize('num, target, expected', [
    ("232", 8, ["2*3+2","2+3*2"]),
    ("105", 5, ["1*0+5","10-5"]),
    ("00", 0, ["0*0","0+0","0-0"]),
    ("3456237490", 9191, []),
])
def test(num, target, expected):
    assert sorted(expected) == sorted(Solution().addOperators(num, target))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
