#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

	Single letters represent a singleton set containing that word.

		R("a") = {"a"}
		R("w") = {"w"}

	When we take a comma-delimited list of two or more expressions, we take the union of possibilities.

		R("{a,b,c}") = {"a","b","c"}
		R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)

	When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.

		R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
		R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

Formally, the three rules for our grammar:

	For every lowercase letter x, we have R(x) = {x}.
	For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
	For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

Example 1:

Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]

Example 2:

Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

Constraints:

	1 <= expression.length <= 60
	expression[i] consists of '{', '}', ','or lowercase English letters.
	The given expression represents a set of words based on the grammar given in the description.
"""
import itertools
from typing import List
import pytest
import sys


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        """May 04, 2024 15:47"""
        N = len(expression)
        def process(i):
            ret = set()
            cur = set()
            while i < N:
                c = expression[i]
                if c == '{':  # sub expression
                    _i, sub = process(i+1)
                    if cur:
                        cur = set([w + _w for w in cur for _w in sub])
                    else:
                        cur = sub
                    i = _i+1
                elif c == ',':
                    ret.update(cur)
                    cur = set()
                    i += 1
                elif c == '}':
                    ret.update(cur)
                    cur = set()
                    return i, ret
                else:
                    j = i
                    while j < N and expression[j] not in '{},':
                        j += 1
                    w = expression[i:j]
                    if i > 0 and expression[i-1] == '}':
                        cur = set([_w + w for _w in cur])
                    else:
                        cur.add(w)
                    i = j
            return i, cur

        _, stack = process(0)
        return sorted(stack)


@pytest.mark.parametrize('args', [
    (("{a,b}{c,{d,e}}", ["ac","ad","ae","bc","bd","be"])),
    (("{{a,z},a{b,c},{ab,z}}", ["a","ab","ac","z"])),
    (("{a,b}c{d,e}f", ["acdf","acef","bcdf","bcef"])),
])
def test(args):
    actual = Solution().braceExpansionII(*args[:-1])
    print()
    print(args[-1])
    print(actual)
    assert args[-1] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
