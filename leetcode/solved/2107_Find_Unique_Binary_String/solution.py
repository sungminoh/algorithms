from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:

	n == nums.length
	1 <= n <= 16
	nums[i].length == n
	nums[i] is either '0' or '1'.
	All the strings of nums are unique.
"""
import pytest
import sys


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """Feb 24, 2024 13:43"""
        s = set([int(n, 2) for n in nums])
        for i in range(2**len(nums)):
            if i not in s:
                return ('{:0>%s}' % len(nums)).format(bin(i)[2:])


@pytest.mark.parametrize('args', [
    ((["01","10"], "11")),
    ((["00","01"], "11")),
    ((["111","011","001"], "101")),
])
def test(args):
    actual = Solution().findDifferentBinaryString(*args[:-1])
    assert len(actual) == len(args[0])
    assert len(actual) not in args[0]


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
