#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Constraints:

	1 <= time.length <= 6 * 104
	1 <= time[i] <= 500
"""
import sys
from collections import defaultdict
from collections import Counter
from typing import List
import pytest


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter(time)
        m = max(counter.keys())
        ret = 0
        for k, v in counter.items():
            for i in range(60 * (k // 60), 2*m+1, 60):
                if i-k in counter:
                    if k == i-k:
                        ret += v*(v-1)
                    else:
                        ret += counter[i-k]*v
        return ret//2

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = [0]*60
        for t in time:
            cnt[t % 60] += 1

        ret = cnt[0]*(cnt[0]-1)//2 + cnt[30]*(cnt[30]-1)//2
        for k in range(1, 30):
            ret += cnt[k]*cnt[60-k]
        return ret


@pytest.mark.parametrize('time, expected', [
    ([30,20,150,100,40], 3),
    ([60,60,60], 3),
])
def test(time, expected):
    assert expected == Solution().numPairsDivisibleBy60(time)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
