#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

	For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:

		place stamp at index 0 of s to obtain "abc??",
		place stamp at index 1 of s to obtain "?abc?", or
		place stamp at index 2 of s to obtain "??abc".

	Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).

We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.

Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".

Constraints:

	1 <= stamp.length <= target.length <= 1000
	stamp and target consist of lowercase English letters.
"""
import sys
from collections import deque
from typing import Tuple
from typing import List
import pytest


class IntervalTree:
    def __init__(self):
        self.tree = []

    def add(self, start, end):
        def insert(arr, start, end):
            if not arr:
                # start, end, min_start, max_end
                return [[start, end, start, end], [], []]
            if start >= arr[0][0]:
                arr[2] = insert(arr[2], start, end)
            else:
                arr[1] = insert(arr[1], start, end)
            arr[0][2] = min(arr[0][2], start)
            arr[0][3] = max(arr[0][3], end)
            return arr

        self.tree = insert(self.tree, start, end)

    def is_covered(self, start, end):
        def cover(arr, start, end):
            if start > end:
                return True
            if not arr or arr[0][2] > start or arr[0][3] < end:
                return False
            if arr[0][1] < start:
                return cover(arr[2], start, end)
            elif end < arr[0][0]:
                return cover(arr[1], start, end)
            return cover(arr[1], start, arr[0][0]-1) and cover(arr[2], arr[0][1]+1, end)

        return cover(self.tree, start, end)

    def not_covered(self, start, end) -> List[Tuple[int, int]]:
        def sub(arr, start, end):
            if start > end:
                return []
            if not arr:
                return [(start, end)]
            if arr[0][1] < start:
                return sub(arr[2], start, end)
            elif end < arr[0][0]:
                return sub(arr[1], start, end)
            return sub(arr[1], start, arr[0][0]-1) + sub(arr[2], arr[0][1]+1, end)

        return sub(self.tree, start, end)


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """04/19/2021 02:14
        Time complexity: O(len(target)*len(stamp))
        Space complexity: O(len(target))

        This returns minimum number of stamps
        """
        def flush(arr, i, pattern):
            arr[i:i+len(pattern)] = [None]*len(pattern)

        def match_forward(arr, i, pattern):
            """Find where to stamp to cover the most letters appear >= i"""
            remain = len(arr)-i
            start_from = max(1, len(pattern)-remain)
            for j in range(start_from, len(pattern)):
                subpattern = pattern[j:]
                if all(a == b for a, b in zip(subpattern, arr[i:i+len(subpattern)])):
                    return i+len(subpattern)-len(pattern)
            return -1

        def match_backward(arr, i, pattern):
            """Find where to stamp to cover the most letters appear < i"""
            remain = i
            end_at = min(len(pattern)-1, i)
            for j in range(end_at, 0, -1):
                subpattern = pattern[0:j]
                if all(a == b for a, b in zip(subpattern, arr[i-len(subpattern):i])):
                    return i-len(subpattern)
            return -1

        def expand(pattern, arr, i, j, ret):
            """Expand forward and backward"""
            while j < len(arr):
                j_ = match_forward(arr, j, pattern)
                if j_ < 0:
                    break
                ret.append(j_)
                flush(arr, j_, pattern)
                j = j_+len(pattern)
            while i > 0:
                i_ = match_backward(arr, i, pattern)
                if i_ < 0:
                    break
                ret.append(i_)
                flush(arr, i_, pattern)
                i = i_

        matches = [m.start() for m in re.finditer(stamp, target)]
        ret = []
        ret.extend(matches)
        arr = list(target)
        # 1. find all exact matches and flush them out
        for s in matches:
            flush(arr, s, stamp)
        # 2. expand from each exact match
        for s in matches:
            expand(stamp, arr, s, s+len(stamp), ret)
        # 3. remove remainders. these are in valley between two exact matches
        i = 0
        while i < len(arr):
            j = i
            while j < len(arr) and arr[j] is not None:
                j += 1
            if i != j:
                idx = stamp.find(''.join(arr[i:j]))
                stamp_at = i - idx
                # stamp must be fully contained in the boundaries
                if idx >= 0 and stamp_at+len(stamp) < len(arr):
                    ret.append(stamp_at)
                else:
                    return []
            i = j+1

        ret.reverse()
        return ret

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """09/02/2022 22:56"""
        m, n = len(target), len(stamp)
        start_indexes = deque([])
        prefix_match = [0] * m
        for i in range(m-n+1):
            cnt = 0
            for j in range(n):
                if stamp[j] != target[i+j]:
                    break
                cnt += 1
            if cnt == n:
                start_indexes.append(i)
            prefix_match[i] = cnt
        suffix_match = [0] * m
        for i in range(m-1, n-2, -1):
            cnt = 0
            for j in range(n):
                if stamp[n-1-j] != target[i-j]:
                    break
                cnt += 1
            suffix_match[i] = cnt

        tree = IntervalTree()
        ret = []
        while start_indexes:
            # current cover
            s = start_indexes.popleft()
            e = s+n-1
            if tree.is_covered(s, e):
                continue
            tree.add(s, e)
            ret.append(s)
            # expand to left
            left_expansion = None
            for l in range(s-1, max(0, s-n)-1, -1):
                if l+prefix_match[l] >= s:
                    left_expansion = l
            if left_expansion is not None:
                start_indexes.append(left_expansion)
            # expand to right
            right_expansion = None
            for r in range(e+1, min(m-1, e+n)+1):
                if r-suffix_match[r] <= e:
                    right_expansion = r
            if right_expansion is not None:
                start_indexes.append(right_expansion-n+1)

        # valley
        for s, e in tree.not_covered(0, len(target)-1):
            i = stamp.find(target[s:e+1])
            if i >= 0 and s-i >= 0 and s-i+len(stamp) < len(target):
                ret.append(s-i)
            else:
                return []

        return ret[::-1]


def decode(stamp, stamp_orders):
    if not stamp_orders:
        return ''
    stamp = list(stamp)
    ret = ['_'] * (max(stamp_orders) + len(stamp))
    for i in stamp_orders:
        ret[i:i+len(stamp)] = stamp
    return ''.join(ret)


@pytest.mark.parametrize('stamp, target, expected', [
    ("abc", "ababc", [0,2]),
    ("abca", "aabcaca", [3,0,1]),
    ("h", "hhhhh", [4,3,2,1,0]),
    ("oz", "ooozz", [0,1,3,2]),
    ("wy", "wwywy", [0,3,1]),
    ("cab", "cabbb", [2,1,0]),
    ("zbs", "zbzbsbszbssbzbszbsss", [10, 17, 16, 8, 0, 4, 15, 12, 7, 2]),
    ("bedaefaeddccbce", "bebedabebbedaefaeddccbced", [])
])
def test(stamp, target, expected):
    actual = Solution().movesToStamp(stamp, target)
    decoded = decode(stamp, actual)
    assert len(expected) == len(actual)
    assert len(expected) == 0 or target == decoded


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
