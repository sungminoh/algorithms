#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:

Input: nums = [-1]
Output: [0]

Example 3:

Input: nums = [-1,-1]
Output: [0,0]

Constraints:

	1 <= nums.length <= 105
	-104 <= nums[i] <= 104
"""
from pathlib import Path
import json
import bisect
import sys
from typing import Tuple
from typing import List
import pytest


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """06/17/2020 23:01
        Time Complexity: O(n*logn)
        Space Complexity: O(n)
        """
        class TreeNode:
            def __init__(self, v):
                self.val = v
                self.left = None
                self.right = None
                self.cnt = 1

        def insert(root, n):
            while root :
                root.cnt += 1
                if n < root.val:
                    if root.left is None:
                        root.left = TreeNode(n)
                        break
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = TreeNode(n)
                        break
                    else:
                        root = root.right

        def cnt_smaller(root, n):
            ret = 0
            while root:
                if root.val < n:
                    ret += 1
                    if root.left:
                        ret += root.left.cnt
                    root = root.right
                else:
                    root = root.left
            return ret

        if not nums:
            return []
        root = TreeNode(nums[-1])
        ret = [0]
        for i in range(len(nums)-2, -1, -1):
            insert(root, nums[i])
            ret.append(cnt_smaller(root, nums[i]))
        return list(reversed(ret))

    def countSmaller(self, nums: List[int]) -> List[int]:
        """06/17/2020 23:06
        Time Complexity: O(n*(logn+n)) considering insertion
        Space Complexity: O(n)
        """
        def binsearch(nums, n):
            i, j = 0, len(nums)-1
            while i <= j:
                m = i + (j-i)//2
                if n <= nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            return i

        if not nums:
            return []
        ret = [0]
        ordered = [nums[-1]]
        for n in nums[-2::-1]:
            i = binsearch(ordered, n)
            ordered.insert(i, n)
            ret.append(i)
        return ret[::-1]

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Binary search
        Time Complexity: O(n*(logn+n)) considering insertion
        Space complexity: O(n)
        """
        ret = []
        arr = []
        for n in reversed(nums):
            i = bisect.bisect_left(arr, n)
            ret.append(i)
            arr.insert(i, n)
        return ret[::-1]

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Merge sort
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        cnt = [0]*len(nums)

        def merge(
            a: List[Tuple[int, int]],
            b: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            i = j = 0
            ret = []
            while i < len(a) or j < len(b):
                if i == len(a):
                    ret.append(b[j])
                    j += 1
                elif j == len(b):
                    cnt[a[i][0]] += j
                    ret.append(a[i])
                    i += 1
                else:
                    if a[i][1] <= b[j][1]:
                        ret.append(a[i])
                        cnt[a[i][0]] += j
                        i += 1
                    else:
                        ret.append(b[j])
                        j += 1
            return ret

        def msort(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(arr) <= 1:
                return arr
            m = len(arr)//2
            return merge(msort(arr[:m]), msort(arr[m:]))

        msort(list(enumerate(nums)))
        return cnt

    def countSmaller(self, nums: List[int]) -> List[int]:
        """08/09/2021 00:03
        Binary indexed tree
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        def query(tree, i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i&-i  # go to parent, remove the least significant 1
            return s

        def update(tree, i):
            while i < len(tree):
                tree[i] += 1
                i += i&-i  # go to next

        m = {n: i for i, n in enumerate(sorted(set(nums)))}
        tree = [0] * len(m)
        ret = []
        for n in reversed(nums):
            ret.append(query(tree, m[n]))
            update(tree, m[n]+1)
        return ret[::-1]

    def countSmaller(self, nums: List[int]) -> List[int]:
        """07/31/2022 23:49"""
        def bisearch(arr, x):
            s, e = 0, len(arr)-1
            while s <= e:
                m = s + ((e-s)//2)
                if arr[m] < x:
                    s = m+1
                else:
                    e = m-1
            return s

        ret = []
        sorted_list = []
        for i in range(len(nums)-1, -1, -1):
            cnt = bisearch(sorted_list, nums[i])
            sorted_list.insert(cnt, nums[i])
            ret.append(cnt)
        return ret[::-1]


@pytest.mark.parametrize('nums, expected', [
    ([5,2,6,1], [2,1,1,0]),
    ([-1], [0]),
    ([-1,-1], [0,0]),
    ([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41],
     [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]),
    json.load(open(Path(__file__).parent/'testcase.json')),
])
def test(nums, expected):
    assert expected == Solution().countSmaller(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
