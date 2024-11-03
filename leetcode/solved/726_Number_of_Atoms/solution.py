#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

	For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.

Two formulas are concatenated together to produce another formula.

	For example, "H2O2He3Mg4" is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.

	For example, "(H2O2)" and "(H2O2)3" are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Constraints:

	1 <= formula.length <= 1000
	formula consists of English letters, digits, '(', and ')'.
	formula is always valid.
"""
from typing import Dict
from typing import Tuple
from collections import Counter
import string
import pytest
import sys


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """11/06/2022 17:14"""
        U = set(string.ascii_uppercase)
        L = set(string.ascii_lowercase)

        def process(i) -> Tuple[int, Dict[str, int]]:
            counter = Counter()
            while i < len(formula):
                c = formula[i]
                if c == '(':
                    j, sub = process(i+1)
                    k = j
                    while k < len(formula) and formula[k].isdigit():
                        k += 1
                    mul = int(formula[j:k]) if k != j else 1
                    for atom, n in sub.items():
                        counter[atom] += n*mul
                    i = k
                elif c == ')':
                    return i+1, counter
                elif c in U:
                    j = i+1
                    while j < len(formula) and formula[j] in L:
                        j += 1
                    atom = formula[i:j]
                    k = j
                    while k < len(formula) and formula[k].isdigit():
                        k += 1
                    cnt = int(formula[j:k]) if k != j else 1
                    counter[atom] += cnt
                    i = k
            return i, counter

        counter = process(0)[1]
        return ''.join(
            f'{atom}{counter[atom]}' if counter[atom] > 1 else atom
            for atom in sorted(counter.keys()))

    def countOfAtoms(self, formula: str) -> str:
        """Jul 29, 2024 23:08"""
        stack = [{}]
        N = len(formula)
        i = 0

        def get_cnt(i):
            cnt = 0
            while i < N and formula[i].isdigit():
                cnt *= 10
                cnt += int(formula[i])
                i += 1
            cnt = max(cnt, 1)
            return i, cnt

        def get_alpha(i):
            k = formula[i]
            i += 1
            while i < N and formula[i] in string.ascii_lowercase:
                k += formula[i]
                i += 1
            return i, k

        while i < N:
            if formula[i] == ')':
                i += 1
                i, cnt = get_cnt(i)
                for k, v in stack.pop().items():
                    stack[-1].setdefault(k, 0)
                    stack[-1][k] += v * cnt
            elif formula[i] == '(':
                stack.append({})
                i += 1
            else:
                assert formula[i] in string.ascii_uppercase
                i, k = get_alpha(i)
                i, cnt = get_cnt(i)
                stack[-1].setdefault(k, 0)
                stack[-1][k] += cnt

        assert len(stack) == 1
        return ''.join(f'{k}{v}' if v > 1 else k for k, v in sorted(stack[-1].items()))


@pytest.mark.parametrize('args', [
    (("H2O", "H2O")),
    (("Mg(OH)2", "H2MgO2")),
    (("K4(ON(SO3)2)2", "K4N2O14S4")),
])
def test(args):
    assert args[-1] == Solution().countOfAtoms(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
