#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.



Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
from itertools import zip_longest

def pp(nums1, nums2, i, j):
    l1, r1 = nums1[:i+1], nums1[i+1:]
    l2, r2 = nums2[:j+1], nums2[j+1:]
    line1 = []
    line2 = []
    for a, b in reversed(list(zip_longest(reversed(l1), reversed(l2), fillvalue=' '))):
        line1.append(a)
        line2.append(b)
    line1.append('(%s)' % i)
    line2.append('(%s)' % j)
    for a, b in zip_longest(r1, r2, fillvalue=''):
        line1.append(a)
        line2.append(b)
    print(' '.join('%2s' % x for x in line1))
    print(' '.join('%2s' % x for x in line2))


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Assure that nums1 is longer than nums1
        if len(nums2) > len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        # If one is less than the other, just concat and find mid
        if nums1 and nums2:
            if nums1[-1] <= nums2[0]:
                return self.findMedianSortedArrays(nums1+nums2, [])
            elif nums2[-1] <= nums1[0]:
                return self.findMedianSortedArrays(nums2+nums1, [])
        # If one is empty, find mid of the other.
        m = len(nums1)
        n = len(nums2)
        if n == 0:
            i, remainder = divmod(m, 2)
            if remainder == 1:
                return nums1[i]
            else:
                return (nums1[i] + nums1[i-1])/2

        # nums1: [0, 1, ......, i, i+1, ......., m-1]
        # nums2:    [0, 1, ..., j, j+1, ... n-1]
        # i + j + 2 = m-1-i + n-1-j (+1 if m+n is odd) -> i = (m+n+1)/2 - j - 2
        l, r = 0, n
        j = (l+r)//2
        i = (m+n+1)//2 -j -2
        while l <= r:
            if nums2[j] > nums1[i+1]:
                r = j-1
            elif j+1 < n and nums2[j+1] < nums1[i]:
                l = j+1
            else:
                break
            j = (l+r)//2
            i = (m+n+1)//2 -j -2

        if j < 0: ml = nums1[i]
        elif i < 0: ml = nums2[j]
        else: ml = max(nums1[i], nums2[j])

        if i+1 >= m: mr = nums2[j+1]
        elif j+1 >= n: mr = nums1[i+1]
        else: mr = min(nums1[i+1], nums2[j+1])

        if (m+n) % 2:
            return ml
        else:
            return (ml + mr) / 2



def main():
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    print(Solution().findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()
