#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

Constraints:

	1 <= nums1.length <= nums2.length <= 1000
	0 <= nums1[i], nums2[i] <= 104
	All integers in nums1 and nums2 are unique.
	All the integers of nums1 also appear in nums2.

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""
import sys
from heapq import heappush
from heapq import heappop
from typing import List
import pytest


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Use heap"""
        table = {n: i for i, n in enumerate(nums2)}

        next_greater_element_index = {}
        heap = []
        for i, n in enumerate(nums2):
            while heap and heap[0][0] < n:
                _, j = heappop(heap)
                next_greater_element_index[j] = i
            heappush(heap, (n, i))

        ret = []
        for n in nums1:
            if n not in table or table[n] not in next_greater_element_index:
                ret.append(-1)
                continue
            ret.append(nums2[next_greater_element_index[table[n]]])
        return ret


    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Use stack"""
        next_greater_num = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                m = stack.pop()
                next_greater_num[m] = n
            stack.append(n)

        return [next_greater_num.get(n, -1) for n in nums1]


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([4,1,2], [1,3,4,2], [-1,3,-1]),
    ([2,4], [1,2,3,4], [3,-1]),
])
def test(nums1, nums2, expected):
    assert expected == Solution().nextGreaterElement(nums1, nums2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
