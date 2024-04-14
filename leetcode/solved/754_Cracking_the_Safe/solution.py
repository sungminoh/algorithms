#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].

The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.

	For example, the correct password is "345" and you enter in "012345":

		After typing 0, the most recent 3 digits is "0", which is incorrect.
		After typing 1, the most recent 3 digits is "01", which is incorrect.
		After typing 2, the most recent 3 digits is "012", which is incorrect.
		After typing 3, the most recent 3 digits is "123", which is incorrect.
		After typing 4, the most recent 3 digits is "234", which is incorrect.
		After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.

Return any string of minimum length that will unlock the safe at some point of entering it.

Example 1:

Input: n = 1, k = 2
Output: "10"
Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.

Example 2:

Input: n = 2, k = 2
Output: "01100"
Explanation: For each possible password:
- "00" is typed in starting from the 4th digit.
- "01" is typed in starting from the 1st digit.
- "10" is typed in starting from the 3rd digit.
- "11" is typed in starting from the 2nd digit.
Thus "01100" will unlock the safe. "10011", and "11001" would also unlock the safe.

Constraints:

	1 <= n <= 4
	1 <= k <= 10
	1 <= kn <= 4096
"""
import itertools
import pytest
import sys


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(map(str, range(k)))

        seen = set()

        def dfs(acc):
            if len(seen) == pow(k, n):
                return acc

            for i in range(k):
                password = f'{acc[-(n-1):]}{i}'
                if password not in seen:
                    seen.add(password)
                    ret = dfs(acc + str(i))
                    if ret:
                        return ret
                    seen.remove(password)

        return dfs('0'*(n-1))


@pytest.mark.parametrize('args', [
    ((1, 2, "10")),
    ((2, 2, "01100")),
    ((2, 5, '00102030411213142232433440'))
])
def test(args):
    n, k = args[0], args[1]

    def iterall(n, k):
        if n == 0:
            yield ''
        else:
            for x in iterall(n-1, k):
                for i in range(k):
                    yield f'{i}{x}'

    actual = Solution().crackSafe(*args[:-1])
    assert len(args[-1]) == len(actual)
    for x in iterall(n, k):
        assert x in actual, x


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
