import itertools
from collections import defaultdict
from collections import Counter
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

	answer[0] is a list of all players that have not lost any matches.
	answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:

	You should only consider the players that have played at least one match.
	The testcases will be generated such that no two matches will have the same outcome.

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

Constraints:

	1 <= matches.length <= 105
	matches[i].length == 2
	1 <= winneri, loseri <= 105
	winneri != loseri
	All matches[i] are unique.
"""
import pytest
import sys


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """Dec 04, 2022 20:14"""
        lost = defaultdict(int)
        for w, l in matches:
            lost[w] += 0
            lost[l] += 1
        answer = [[], []]
        for i in sorted(lost.keys()):
            if lost[i] > 1:
                continue
            answer[lost[i]].append(i)
        return answer

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """Jan 24, 2024 19:57"""
        players = set(itertools.chain(*matches))
        lose_cnt = Counter(x[1] for x in matches)
        ret = [
            sorted(list(players - set(lose_cnt.keys()))),
            []
        ]
        for loser in sorted(lose_cnt.keys()):
            if lose_cnt[loser] == 1:
                ret[1].append(loser)
        return ret


@pytest.mark.parametrize('args', [
    (([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]], [[1,2,10],[4,5,7,8]])),
    (([[2,3],[1,3],[5,4],[6,4]], [[1,2,5,6],[]])),
])
def test(args):
    assert args[-1] == Solution().findWinners(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
