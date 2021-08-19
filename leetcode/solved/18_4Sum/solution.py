#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

	0 <= a, b, c, d < n
	a, b, c, and d are distinct.
	nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

	1 <= nums.length <= 200
	-109 <= nums[i] <= 109
	-109 <= target <= 109
"""
from functools import lru_cache
import sys
import itertools
from typing import List
import pytest


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(2^n)
        Space complexity: O(n^4)
        """
        ret = set()

        def dfs(i, cur, backtrack):
            if len(nums)-i < 4-len(backtrack):
                return
            if len(backtrack) == 4:
                if cur == target:
                    ret.add(tuple(sorted(backtrack)))
                return
            dfs(i+1, cur, backtrack)
            dfs(i+1, cur+nums[i], backtrack + [nums[i]])

        dfs(0, 0, [])
        return [list(x) for x in ret]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(n^4)
        Space complexity: O(n^4)
        """
        nums.sort()
        ret = set()

        @lru_cache(None)
        def dfs(cur, used, cnt):
            if cnt == 4:
                if cur == target:
                    arr = []
                    i = 0
                    while used:
                        if used % 2:
                            arr.append(nums[i])
                        used //= 2
                        i += 1
                    ret.add(tuple(arr))
                return

            for i, n in enumerate(nums):
                if not used & 1<<i:
                    dfs(cur + nums[i], used | 1<<i, cnt+1)

        dfs(0, 0, 0)
        return [list(x) for x in ret]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time complexity: O(n^3)
        """
        if len(nums) < 4:
            return []
        ret = set()
        nums.sort()
        s = 0
        for i in range(len(nums)-3):
            s += nums[i]
            for j in range(i+1, len(nums)-2):
                s += nums[j]
                l, r = j+1, len(nums)-1
                while l < r:
                    sub = nums[l] + nums[r]
                    s += sub
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        quadruplets = (nums[i], nums[j], nums[l], nums[r])
                        ret.add(quadruplets)
                        while l < len(nums) and nums[l] == quadruplets[-2]: l += 1
                        while r >= 0 and nums[r] == quadruplets[-1]: r -= 1
                    s -= sub
                s -= nums[j]
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
            s -= nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        return [list(x) for x in ret]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Generic version
        Time complexity: O(n^3)
        """
        N = 4
        if len(nums) < N:
            return []
        nums.sort()

        def next_pointer(pointer, n):
            i = -1
            while -i <= len(pointer) and pointer[i] == n+i:
                i -= 1
            if -i > len(pointer):
                return None
            pointer[i:] = list(range(pointer[i]+1, pointer[i]+1-i))
            return pointer

        ret = set()
        pointer = list(range(N-2))
        while pointer:
            pre = [nums[p] for p in pointer]
            s = sum(pre)
            l, r = pointer[-1]+1, len(nums)-1
            while l < r:
                sub = nums[l] + nums[r]
                s += sub
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    arr = (*pre, nums[l], nums[r])
                    ret.add(arr)
                    while l < len(nums) and nums[l] == arr[-2]: l += 1
                    while r >= 0 and nums[r] == arr[-1]: r -= 1
                s -= sub
            pointer = next_pointer(pointer, len(nums)-2)
        return [list(x) for x in ret]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Generic version
        Time complexity: O(n^3)
        """
        N = 4
        if len(nums) < N:
            return []

        def sum_k(i, j, target, k):
            # accelerate
            if j-i+1 < k or sum(nums[i:i+k]) > target or sum(nums[j+1-k:j+1]) < target:
                return []
            if k == 2:
                ret = []
                while i < j:
                    s = nums[i] + nums[j]
                    if s < target:
                        i += 1
                    elif s > target:
                        j -= 1
                    else:
                        ret.append([nums[i], nums[j]])
                        while i < j and ret[-1][-2] == nums[i]: i += 1
                        while i < j and ret[-1][-1] == nums[j]: j -= 1
                return ret
            ret = []
            for m in range(i, j+1):
                if m > i and nums[m-1] == nums[m]:
                    continue
                ret.extend([[nums[m]] + x for x in sum_k(m+1, j, target-nums[m], k-1)])
            return ret

        nums.sort()
        return sum_k(0, len(nums)-1, target, N)


    # ([-498,-492,-473,-455,-441,-412,-390,-378,-365,-359,-358,-326,-311,-305,-277,-265,-264,-256,-254,-240,-237,-234,-222,-211,-203,-201,-187,-172,-164,-134,-131,-91,-84,-55,-54,-52,-50,-27,-23,-4,0,4,20,39,45,53,53,55,60,82,88,89,89,98,101,111,134,136,209,214,220,221,224,254,281,288,289,301,304,308,318,321,342,348,354,360,383,388,410,423,442,455,457,471,488,488], -2808, []),
    # ([-497,-494,-484,-477,-453,-453,-444,-442,-428,-420,-401,-393,-392,-381,-357,-357,-327,-323,-306,-285,-284,-263,-262,-254,-243,-234,-208,-170,-166,-162,-158,-136,-133,-130,-119,-114,-101,-100,-86,-66,-65,-6,1,3,4,11,69,77,78,107,108,108,121,123,136,137,151,153,155,166,170,175,179,211,230,251,255,266,288,306,308,310,314,321,322,331,333,334,347,349,356,357,360,361,361,367,375,378,387,387,408,414,421,435,439,440,441,470,492], 1682, [[331, 440, 441, 470], [408, 414, 421, 439], [333, 439, 440, 470], [347, 408, 435, 492], [357, 414, 441, 470], [367, 435, 439, 441], [387, 421, 435, 439], [356, 421, 435, 470], [310, 439, 441, 492], [314, 435, 441, 492], [361, 408, 421, 492], [306, 414, 470, 492], [334, 421, 435, 492], [333, 387, 470, 492], [387, 414, 440, 441]]),
    # ([-499,-486,-479,-462,-456,-430,-415,-413,-399,-381,-353,-349,-342,-337,-336,-331,-330,-322,-315,-280,-271,-265,-249,-231,-226,-219,-216,-208,-206,-204,-188,-159,-144,-139,-123,-115,-99,-89,-80,-74,-61,-22,-22,-8,-5,4,43,65,82,86,95,101,103,123,149,152,162,165,168,183,204,209,209,220,235,243,243,244,248,253,260,273,281,284,288,290,346,378,382,384,407,411,423,432,433,445,470,476,497], 3032, []),
@pytest.mark.parametrize('nums, target, expected', [
    ([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
    ([2,2,2,2,2], 8, [[2,2,2,2]]),
    ([-5,5,4,-3,0,0,4,-2], 4, [[-5,0,4,5],[-3,-2,4,5]]),
    ([0], 0, []),
    ([-3,-2,-1,0,0,1,2,3], 0, [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
])
def test(nums, target, expected):
    actual = Solution().fourSum(nums, target)
    print(actual)
    assert sorted(sorted(x) for x in expected) == sorted(sorted(x) for x in actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
