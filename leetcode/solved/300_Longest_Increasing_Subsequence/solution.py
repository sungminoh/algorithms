#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lis = [nums[0]]
        for n in nums[1:]:
            smaller_idx = self.bisearch(lis, n)
            if smaller_idx + 1 == len(lis):
                lis.append(n)
            elif lis[smaller_idx + 1] > n:
                lis[smaller_idx + 1] = n
        return len(lis)

    def bisearch(self, arr, n):
        left, right = 0, len(arr) - 1
        while right - left >= 0:
            mid = left + (right - left) // 2
            if arr[mid] >= n:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def lengthOfLISnn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lis = [1] * len(nums)
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[:i]):
                if m < n:
                    lis[i] = max(lis[i], lis[j] + 1)
        print(lis)
        return max(lis)


if __name__ == '__main__':
    cases = [
        ([10,9,2,5,3,7,101,18], 4),
        ([10,9,2,5,3,4], 3)
    ]
    for case, expected in cases:
        actual = Solution().lengthOfLIS(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
