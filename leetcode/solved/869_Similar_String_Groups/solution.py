from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:

Input: strs = ["omv","ovm"]
Output: 1

Constraints:

	1 <= strs.length <= 300
	1 <= strs[i].length <= 300
	strs[i] consists of lowercase letters only.
	All words in strs have the same length and are anagrams of each other.
"""
import pytest
import sys


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        """Sep 04, 2023 13:13"""
        def is_simliar(a, b):
            used = False
            found = None
            for x, y in zip(a, b):
                if x == y:
                    continue
                if used:
                    return False
                if not found:
                    found = (x, y)
                else:
                    if found != (y, x):
                        return False
                    used = True
            return True

        N = len(strs)
        reps = [i for i in range(N)]
        def find(i):
            if reps[i] == i:
                return i
            reps[i] = find(reps[i])
            return reps[i]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            reps[ra] = reps[rb] = min(ra, rb)

        for i in range(N):
            for j in range(i+1, N):
                if is_simliar(strs[i], strs[j]):
                    union(i, j)

        for i in range(N):
            reps[i] = find(i)

        return len(set(reps))


@pytest.mark.parametrize('args', [
    ((["tars","rats","arts","star"], 2)),
    ((["omv","ovm"], 1)),
    ((["jvhpg","jhvpg","hpvgj","hvpgj","vhgjp"], 3)),
    ((["ajdidocuyh","djdyaohuic","ddjyhuicoa","djdhaoyuic","ddjoiuycha","ddhoiuycja","ajdydocuih","ddjiouycha","ajdydohuic","ddjyouicha"], 2)),
])
def test(args):
    assert args[-1] == Solution().numSimilarGroups(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
