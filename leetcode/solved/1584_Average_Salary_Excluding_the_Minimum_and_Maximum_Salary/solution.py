#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

Constraints:

	3 <= salary.length <= 100
	1000 <= salary[i] <= 106
	All the integers of salary are unique.
"""
from typing import List
import pytest
import sys


class Solution:
    def average(self, salary: List[int]) -> float:
        """Sep 09, 2023 21:22"""
        minmax = {min(salary), max(salary)}
        acc = 0
        cnt = 0
        for s in salary:
            if s not in minmax:
                acc += s
                cnt += 1
        return acc/cnt


@pytest.mark.parametrize('args', [
    (([4000,3000,1000,2000], 2500.00000)),
    (([1000,2000,3000], 2000.00000)),
])
def test(args):
    assert args[-1] == Solution().average(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
