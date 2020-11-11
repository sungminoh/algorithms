#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""
from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def calc(operator, left, right):
            if operator == '*':
                return left * right
            if operator == '+':
                return left + right
            if operator == '-':
                return  left - right
            raise Exception('Operator not found', operator)

        def parse_expr(s):
            equation = []
            i = 0
            while i < len(s):
                j = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                if j != i:
                    equation.append(int(s[j:i]))
                if i < len(s):
                    equation.append(s[i])
                i += 1
            return equation

        equation = parse_expr(input)
        # print(equation)

        @lru_cache(None)
        def diff_ways_to_compute(i, j):
            print(i, j)
            if i + 1 == j:
                return [equation[i]]
            ret = []
            for p in range(i + 1, j, 2):
                left = diff_ways_to_compute(i, p)
                right = diff_ways_to_compute(p + 1, j)
                for l in left:
                    for r in right:
                        ret.append(calc(equation[p], l, r))
            return ret
        return sorted(diff_ways_to_compute(0, len(equation)))


def main():
    cases = [
        ("2-1-1", [0, 2]),
        ("2*3-4*5", [-34, -14, -10, -10, 10]),
        ("10+5", [15])
    ]
    for case, expected in cases:
        actual = Solution().diffWaysToCompute(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
