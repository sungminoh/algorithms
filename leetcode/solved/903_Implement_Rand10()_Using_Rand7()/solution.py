
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

Example 1:

Input: 1
Output: [7]

Example 2:

Input: 2
Output: [8,4]

Example 3:

Input: 3
Output: [8,1,10]

Note:

	rand7 is predefined.
	Each testcase has one argument: n, the number of times that rand10 is called.

Follow up:

	What is the expected value for the number of calls to rand7() function?
	Could you minimize the number of calls to rand7()?
"""
import sys
from collections import Counter
import random
import pytest


# The rand7() API is already defined for you.
def rand7():
    # @return a random integer in the range 1 to 7
    return random.randint(1, 7)


class Solution:
    def rand5(self):
        k = rand7()
        while k > 5:
            k = rand7()
        return k

    def rand2(self):
        k = rand7()
        while k == 7:
            k = rand7()
        return (k % 2) + 1

    def rand10(self):
        while True:
            # 0 to 48
            n = (rand7() - 1) * 7 + (rand7() - 1)
            if n >= 40:
                continue
            else:
                return n % 10 + 1

    def _rand10(self):
        """
        :rtype: int
        """
        return 2 * self.rand5() - (self.rand2() - 1)


def test():
    s = Solution()
    print(Counter(s.rand10() for _ in range(100000)))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
