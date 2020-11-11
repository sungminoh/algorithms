#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.

Example 2:

Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Constraints:

	bottom will be a string with length in range [2, 8].
	allowed will have length in range [0, 200].
	Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
"""
import sys
from functools import lru_cache
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = defaultdict(set)
        for t in allowed:
            m[t[:2]].add(t[2])

        @lru_cache(None)
        def reduce(s):
            if len(s) == 1:
                return ['']
            ret = []
            for c in m.get(s[:2], {}):
                ret.extend(c + sub for sub in reduce(s[1:]))
            return ret

        @lru_cache(None)
        def reducible(s):
            if len(s) == 1:
                return True
            if s[:2] not in m:
                return False
            return any(reducible(sub) for sub in reduce(s))

        return reducible(bottom)

    def _pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = defaultdict(set)
        for t in allowed:
            m[t[:2]].add(t[2])

        # @lru_cache(None)
        def possibles(a, side):
            if not side:
                yield a
            else:
                for c in m.get(a+side[0], {}):
                    for s in possibles(c, side[1:]):
                        yield a + s

        # @lru_cache(None)
        def reduce(s):
            if len(s) == 1:
                yield s
            if s[:2] not in m:
                return
            for side in reduce(s[1:]):
                yield from possibles(s[0], side)

        result = list(reduce(bottom))
        # print(result)
        return True if result else False


@pytest.mark.parametrize('bottom, allowed, expected', [
    ("BCD", ["BCG", "CDE", "GEA", "FFF"], True),
    ("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"], False),
    ("BDAFFFDB", ["EED", "BGG", "AGF", "AGD", "AGA", "CCE", "DCG", "DCD", "DCB", "DCA", "FGD", "FGE", "FGG", "FGA", "FGC", "BFB", "BFG", "BFD", "FAB", "GAF", "EDD", "DBC", "EDE", "DBE", "DBD", "FAG", "FFG", "FFF", "FFE", "FFD", "FFC", "FFA", "FDA", "GCA", "GBD", "FDB", "GBB", "BEB", "BEF", "BEG", "BED", "AEA", "GCB", "AED", "AEG", "AEF", "DEA", "EEA", "DEE", "DEF", "EEB", "CEG", "CEC", "GEC", "GEB", "GEG", "GED", "BDE", "BDG", "BDF", "GCE", "AFE", "AFG", "AFA", "AFB", "EFA", "DDA", "EFD", "DDF", "EFF", "EFG", "CBB", "CBF", "CBD", "BDA", "ACC", "ACB", "ACA", "ACE", "BCE", "BCF", "BCG", "DGF", "ECG", "DGC", "ECE", "ECC", "DGD", "CGA", "CGC", "CGE", "FCB", "FCD", "DDE", "FCF", "GGB", "FED", "FEB", "BBC", "BBA", "ADF", "ADE", "ADB", "ADA", "DFD", "DFA", "DFC", "CDD", "CDE", "CDB", "CDC", "FBC", "GDB", "GDC", "FBG", "GDE", "AAE", "AAD", "AAG", "AAA", "AAC", "BAF", "BAG", "BAB", "BAA", "CAC", "CAB", "CAE", "CAD", "DAF", "DAB", "DAC", "EAC", "EAF", "GAG", "FAC", "FAF", "GAB", "ABB", "ABD", "ABE", "ABF", "ABG", "GCC", "EBD", "EBE", "EBF", "CFF", "CFE", "CFB", "GFA", "GFF", "GFG"], True),
    ("BCD", ["ACC","ACB","ABD","DAA","BDC","BDB","DBC","BBD","BBC","DBD","BCC","CDD","ABA","BAB","DDC","CCD","DDA","CCA","DDD"], True),
])
def test(bottom, allowed, expected):
    assert expected == Solution().pyramidTransition(bottom, allowed)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
