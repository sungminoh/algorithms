#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

Example 2:

Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

Constraints:

	n == nums.length
	m == queries.length
	1 <= n, m <= 1000
	1 <= nums[i], queries[i] <= 106
"""
import itertools
import bisect
from typing import List
import pytest
import sys


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """Feb 19, 2023 20:29"""
        length_sum = enumerate(itertools.accumulate(sorted(nums)), 1)
        sum_length = {s: l for l, s in length_sum}
        thresholds = list(sorted(sum_length.keys()))
        ret = []
        for q in queries:
            i = bisect.bisect_right(thresholds, q)-1
            if 0 <= i < len(thresholds):
                ret.append(sum_length[thresholds[i]])
            else:
                ret.append(0)
        return ret


@pytest.mark.parametrize('nums, queries, expected', [
    ([4,5,2,1], [3,10,21], [2,3,4]),
    ([2,3,4,5], [1], [0]),
])
def test(nums, queries, expected):
    assert expected == Solution().answerQueries(nums, queries)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
