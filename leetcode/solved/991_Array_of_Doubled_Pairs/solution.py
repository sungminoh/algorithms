#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:

Input: arr = [3,1,3,6]
Output: false

Example 2:

Input: arr = [2,1,2,6]
Output: false

Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:

Input: arr = [1,2,4,16,8,4]
Output: false

Constraints:

	2 <= arr.length <= 3 * 104
	arr.length is even.
	-105 <= arr[i] <= 105
"""
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = Counter(A)
        for a in sorted(cnt.keys(), key=abs):
            if cnt[a] > cnt[2 * a]:
                return False
            cnt[2 * a] -= cnt[a]
        return True

    def canReorderDoubled(self, A: List[int]) -> bool:
        """05/30/2020 13:16"""
        cnt = Counter(A)
        if 0 in cnt and cnt[0] % 2 == 0:
            cnt.pop(0)
        while cnt:
            removes = []
            found = False
            for a, c, in cnt.items():
                if c <= 0:
                    continue
                if cnt.get(2 * a, 0) > 0:
                    if a % 2 == 0 and cnt.get(a // 2, 0) > 0:
                        pass
                    else:
                        cnt[2 * a] -= 1
                        cnt[a] -= 1
                        found = True
                        # print(a, 2*a)
                        if cnt[2 * a] == 0:
                            removes.append(2 * a)
                elif a % 2 == 0 and cnt.get(a // 2, 0) > 0:
                    cnt[a // 2] -= 1
                    cnt[a] -= 1
                    # print(a, a//2)
                    found = True
                    if cnt[a // 2] == 0:
                        removes.append(a // 2)
                if cnt[a] == 0:
                    removes.append(a)
            # print(cnt)
            if not found:
                return False
            for a in removes:
                cnt.pop(a)
        return True

    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        for a in sorted(cnt.keys(), key=abs):
            while cnt[a] > 0:
                if cnt[a*2] == 0:
                    return False
                cnt[a] -= 1
                cnt[a*2] -= 1
        return True


@pytest.mark.parametrize('arr, expected', [
    ([3,1,3,6], False),
    ([2,1,2,6], False),
    ([4,-2,2,-4], True),
    ([1,2,4,16,8,4], False),
    ([2,1,2,1,1,1,2,2], True)
])
def test(arr, expected):
    assert expected == Solution().canReorderDoubled(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
