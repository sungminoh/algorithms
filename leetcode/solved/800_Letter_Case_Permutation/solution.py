#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]

Example 3:

Input: S = "12345"
Output: ["12345"]

Example 4:

Input: S = "0"
Output: ["0"]

Constraints:

	S will be a string with length between 1 and 12.
	S will consist only of letters or digits.
"""
import sys
from typing import List
import pytest


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret = []
        chars = list(S)
        def dfs(i):
            if i == len(chars):
                ret.append(''.join(chars))
            else:
                if not chars[i].isdigit():
                    chars[i] = chars[i].lower()
                    dfs(i+1)
                    chars[i] = chars[i].upper()
                dfs(i+1)

        dfs(0)
        return ret


@pytest.mark.parametrize('S, expected', [
    ("a1b2", ["a1b2","a1B2","A1b2","A1B2"]),
    ("3z4", ["3z4","3Z4"]),
    ("12345", ["12345"]),
    ("0", ["0"]),
])
def test(S, expected):
    assert expected == Solution().letterCasePermutation(S)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
