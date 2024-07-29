#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Constraints:

	n == names.length == heights.length
	1 <= n <= 103
	1 <= names[i].length <= 20
	1 <= heights[i] <= 105
	names[i] consists of lower and upper case English letters.
	All the values of heights are distinct.
"""
from typing import List
import pytest
import sys


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """Jul 28, 2024 18:48"""
        return [n for _, n in sorted(zip(heights, names), reverse=True)]


@pytest.mark.parametrize('args', [
    ((["Mary","John","Emma"], [180,165,170], ["Mary","Emma","John"])),
    ((["Alice","Bob","Bob"], [155,185,150], ["Bob","Alice","Bob"])),
])
def test(args):
    assert args[-1] == Solution().sortPeople(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
