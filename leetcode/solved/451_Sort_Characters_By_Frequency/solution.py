
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import sys
from collections import OrderedDict
from collections import Counter
import pytest


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ret = ''
        for c, n in cnt.most_common():
            ret += c * n
        return ret


@pytest.mark.parametrize('s, expected', [
    ('tree', 'eert'),
    ('cccaaa', 'cccaaa'),
    ('Aabb', 'bbAa')
])
def test(s, expected):
    print()
    print(expected, Solution().frequencySort(s))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))


