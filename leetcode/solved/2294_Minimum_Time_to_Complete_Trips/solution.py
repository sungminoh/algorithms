#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

Example 1:

Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0].
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0].
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1].
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

Example 2:

Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.

Constraints:

	1 <= time.length <= 105
	1 <= time[i], totalTrips <= 107
"""
from pathlib import Path
import json
from typing import List
import pytest
import sys


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """Mar 09, 2023 22:11
        TLE
        """
        h = [(t, i) for i, t in enumerate(time)]
        heapify(h)
        t = 0
        while totalTrips:
            t, i = heappop(h)
            heappush(h, (t+time[i], i))
            totalTrips -= 1
        return t

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """Mar 09, 2023 22:21"""
        mn = min(time)
        mx = totalTrips*min(time)

        def bisearch(l, r):
            while l <= r:
                m = l + (r-l)//2
                n = sum(m//t for t in time)
                if n >= totalTrips:
                    r = m-1
                else:
                    l = m+1
            return r+1

        return bisearch(mn, mx)

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """Apr 07, 2023 20:03"""
        l = min(time)
        r = max(l, totalTrips*min(time))
        while l <= r:
            m = l + (r-l)//2
            s = sum(m//t for t in time)
            if s < totalTrips:
                l = m+1
            else:
                r = m-1
        return r+1


@pytest.mark.parametrize('args', [
    (([1,2,3], 5, 3)),
    (([2], 1, 2)),
    (([9,3,10,5], 2, 5)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 5613096, 9310878)),
])
def test(args):
    assert args[-1] == Solution().minimumTime(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
