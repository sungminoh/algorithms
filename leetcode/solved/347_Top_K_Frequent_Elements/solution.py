#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:

	1 <= nums.length <= 105
	-104 <= nums[i] <= 104
	k is in the range [1, the number of unique elements in the array].
	It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """04/09/2020 23:27"""
        cnt = []
        idx = {}
        for n in nums:
            if n not in idx:
                idx[n] = len(cnt)
                cnt.append([n, 1])
            else:
                i = idx[n]
                cnt[i][1] += 1
                while i > 0 and cnt[i-1][1] < cnt[i][1]:
                    cnt[i-1], cnt[i] = cnt[i], cnt[i-1]
                    idx[cnt[i][0]] = i
                    i -= 1
                idx[n] = i
        return [x[0] for x in cnt[:k]]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Apr 20, 2022 12:03"""
        return [x[0] for x in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Apr 20, 2022 13:48"""
        ordered = []
        idx = {}
        for n in nums:
            if n not in idx:
                idx[n] = len(ordered)
                ordered.append([n, 1])
            else:
                ordered[idx[n]][1] += 1
                i = idx[n]-1
                while i >= 0 and ordered[i][1] < ordered[i+1][1]:
                    idx[ordered[i][0]] = i+1
                    idx[ordered[i+1][0]] = i
                    ordered[i], ordered[i+1] = ordered[i+1], ordered[i]
                    i -= 1
        return [x[0] for x in ordered[:k]]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Sep 22, 2023 18:28"""
        counter = {}
        index = {}
        arr = []
        for n in nums:
            if n not in counter:
                counter[n] = 1
                index[n] = len(arr)
                arr.append(n)
            else:
                counter[n] += 1
                i = index[n]
                while i > 0 and counter[arr[i-1]] < counter[n]:
                    index[n] -= 1
                    index[arr[i-1]] += 1
                    arr[i-1], arr[i] = arr[i], arr[i-1]
                    i -= 1
        return arr[:k]


@pytest.mark.parametrize('args', [
    ([1,1,1,2,2,3], 2, [1,2]),
    ([1], 1, [1]),
    ([1,2,3,4,1,2,3,1,2,1], 3, [1,2,3]),
    ([5,3,1,1,1,3,73,1], 1, [1]),
    ([5,3,1,1,1,3,73,1], 2, [1,3]),
    ([4,1,-1,2,-1,2,3], 2, [-1, 2]),
])
def test(args):
    assert sorted(args[-1]) == sorted(Solution().topKFrequent(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
