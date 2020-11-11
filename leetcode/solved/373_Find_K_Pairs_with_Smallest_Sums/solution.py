#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""

import pytest
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                s = n1 + n2
                if len(heap) >= k:
                    if s > -heap[0][0]:
                        break
                    heapq.heappushpop(heap, (-s, [n1, n2]))
                else:
                    heapq.heappush(heap, (-s, [n1, n2]))
        return [x[1] for x in sorted(heap, key=lambda x: -x[0])]


@pytest.mark.parametrize('nums1, nums2, k, expected', [
    ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]),
    ([1,1,2], [1,2,3], 2, [[1,1], [1,1]]),
    ([1,2], [3], 3, [[1,3], [2,3]]),
    ([], [], 5, []),
    ([1,1,2], [1,2,3], 10, [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]),
    ([1,2,4,5,6], [3,5,7,9], 20, [[1,3],[2,3],[1,5],[4,3],[2,5],[5,3],[1,7],[6,3],[4,5],[2,7],[5,5],[1,9],[6,5],[4,7],[2,9],[5,7],[6,7],[4,9],[5,9],[6,9]])
])
def test(nums1, nums2, k, expected):
    print('\n')
    actual = Solution().kSmallestPairs(nums1, nums2, k)
    print(expected)
    print(actual)
    assert [sum(x) for x in expected] == [sum(x) for x in actual]

