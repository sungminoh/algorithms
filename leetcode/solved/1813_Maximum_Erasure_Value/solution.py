#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 104
"""
from collections import deque
import sys
from typing import List
import pytest


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """06/09/2021 05:14"""
        cnt = {}
        deq = deque()
        acc = 0
        ret = -float('inf')
        for n in nums:
            if cnt.get(n, 0) > 0:
                while deq[0] != n:
                    m = deq.popleft()
                    cnt[m] -= 1
                    acc -= m
                deq.popleft()
            else:
                cnt[n] = 1
                acc += n
            deq.append(n)
            ret = max(ret, acc)
        return ret

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pool = set()
        ret = 0
        cur = 0
        j = 0
        for i, n in enumerate(nums):
            if n in pool:
                while nums[j] != n:
                    cur -= nums[j]
                    pool.remove(nums[j])
                    j += 1
                cur -= nums[j]
                j += 1
            pool.add(n)
            cur += n
            ret = max(ret, cur)
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([4,2,4,5,6], 17),
    ([5,2,1,2,5,2,1,2,5], 8),
])
def test(nums, expected):
    assert expected == Solution().maximumUniqueSubarray(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
