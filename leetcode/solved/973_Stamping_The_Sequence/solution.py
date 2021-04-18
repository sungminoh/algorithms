#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]

Note:

	1 <= stamp.length <= target.length <= 1000
	stamp and target only contain lowercase letters.
"""
import sys
import re
from typing import List
import pytest


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        Time complexity: O(len(target)*len(stamp))
        Space complexity: O(len(target))

        This returns minimum number of stamps
        """
        def flush(arr, i, pattern):
            arr[i:i+len(pattern)] = [None]*len(pattern)

        def match_forward(arr, i, pattern):
            """Find where to stamp to cover most letters appear >= i"""
            remain = len(arr)-i
            start_from = max(1, len(pattern)-remain)
            for j in range(start_from, len(pattern)):
                subpattern = pattern[j:]
                if all(a == b for a, b in zip(subpattern, arr[i:i+len(subpattern)])):
                    return i+len(subpattern)-len(pattern)
            return -1

        def match_backward(arr, i, pattern):
            """Find where to stamp to cover th emost letters appear < i"""
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

@pytest.mark.parametrize('stamp, target, expected', [
    ("abc", "ababc", [0,2]),
    ("abca", "aabcaca", [0,3,1]),
    ("h", "hhhhh", [4,3,2,1,0]),
    ("oz", "ooozz", [0,1,3,2]),
    ("wy", "wwywy", [0,3,1]),
    ("cab", "cabbb", [2,1,0]),
    ("zbs", "zbzbsbszbssbzbszbsss", [10, 17, 16, 8, 0, 4, 15, 12, 7, 2]),
    ("bedaefaeddccbce", "bebedabebbedaefaeddccbced", [])
])
def test(stamp, target, expected):
    assert expected == Solution().movesToStamp(stamp, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
