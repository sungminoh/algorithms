#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".

Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".

Constraints:

	1 <= s1.length <= 20
	s2.length == s1.length
	s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
	s2 is an anagram of s1.
"""
import bisect
from typing import List
from collections import deque
import pytest
import sys


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        s1, s2 = list(zip(*[(a, b) for a, b in zip(s1, s2) if a != b]))
        # print()
        # print(''.join(s1))
        # print(''.join(s2))
        # s1 = list(s1)
        # s2 = list(s2)

        def build_char_positions(s):
            ret = {}
            for i, c in enumerate(s):
                ret.setdefault(c, set()).add(i)
            return ret

        char_pos = build_char_positions(s2)

        seen = set()
        def see_parents(parents: List):
            seen.update(parents)
            ret = len(parents)-1
            # print(parents)
            # c = s2[parents[0]]
            # for i in range(len(parents)-1):
            #     s2[parents[i]] = s2[parents[i+1]]
            # s2[parents[-1]] = c
            return ret

        def bfs(i):
            q = deque([(i, [i])])
            while q:
                idx, parents = q.popleft()
                for k in char_pos.get(s1[idx], []):
                    if k == i:
                        ret = see_parents(parents)
                        # print(''.join(s1))
                        # print(''.join(s2))
                        return ret
                    if k not in seen:
                        q.append((k, parents + [k]))
            return 0

        ret = 0
        for i in range(len(s1)):
            if i not in seen:
                ret += bfs(i)
        return ret

    def kSimilarity(self, s1: str, s2: str) -> int:
        """Apr 18, 2024 18:36"""
        if s1 == s2:
            return 0

        s1, s2 = list(zip(*[(a, b) for a, b in zip(s1, s2) if a != b]))
        # s1 = ''.join(s1)
        # s2 = ''.join(s2)

        def build_char_positions(s):
            ret = {}
            for i, c in enumerate(s):
                ret.setdefault(c, []).append(i)
            return ret

        char_pos = build_char_positions(s2)

        def neighbor(s):
            s = list(s)
            for i, c in enumerate(s):
                if s[i] != s2[i]:
                    start = bisect.bisect_right(char_pos[c], i)
                    for _j in range(start, len(char_pos[c])):
                        j = char_pos[c][_j]
                        if s[j] != s2[j]:
                            # yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                            s[i], s[j] = s[j], s[i]
                            yield tuple(s)
                            s[i], s[j] = s[j], s[i]
                    break

        ret = 0
        queue = deque([s1])
        visited = set([s1])
        while queue:
            size = len(queue)
            for _ in range(size):
                s = queue.popleft()
                if s == s2:
                    return ret
                for _s in neighbor(s):
                    if _s not in visited:
                        visited.add(_s)
                        queue.append(_s)
            ret += 1


@pytest.mark.parametrize('args', [
    (("ab", "ba", 1)),
    (("abc", "bca", 2)),
    (("abac", "baca", 2)),
    (("bccaba", "abacbc", 3)),  # bccaa abacc
    (("abccab", "abccab", 0)),
    (("abccaacceecdeea", "bcaacceeccdeaae", 9)),
    (("aabccb", "bbcaca", 3)),
    (("aabbccddee", "cbeddebaac", 6)),
    (("cdebcdeadedaaaebfbcf", "baaddacfedebefdabecc", 12)),
])
def test(args):
    assert args[-1] == Solution().kSimilarity(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
