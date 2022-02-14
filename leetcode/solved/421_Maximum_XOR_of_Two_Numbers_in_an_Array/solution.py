#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Constraints:

	1 <= nums.length <= 2 * 105
	0 <= nums[i] <= 231 - 1
"""
import random
import sys
import math
from typing import List
import pytest


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class Trie:
            class Node:
                def __init__(self):
                    self.chars = {}

            def __init__(self):
                self.root = self.Node()

            def insert(self, n):
                b = '{:032b}'.format(n)
                cur = self.root
                for i in b:
                    if i not in cur.chars:
                        cur.chars[i] = self.Node()
                    cur = cur.chars[i]

        trie = Trie()
        for n in nums:
            trie.insert(n)

        def get_pair(trie, n):
            b = '{:032b}'.format(n)
            m = ''
            cur = trie.root
            for i in b:
                j = '1' if i == '0' else '0'
                if j in cur.chars:
                    m += j
                    cur = cur.chars[j]
                else:
                    m += i
                    cur = cur.chars[i]
            return int(m, 2)

        ret = 0
        for n in nums:
            m = get_pair(trie, n)
            ret = max(ret, n ^ m)
        return ret

    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        From discussion. construct answer from the largest bit
        """
        nums = set(nums)
        m = max(nums)
        if not m:
            return 0
        bit_len = int(math.log2(m))
        ret = 0
        for i in range(bit_len, -1, -1):
            ret <<= 1
            prefixes = {n>>i for n in nums}
            for p in prefixes:
                if (ret + 1) ^ p in prefixes:
                    ret += 1
                    break
        return ret

    def findMaximumXOR(self, nums: List[int]) -> int:
        def divide(group, bit):
            ret = [[], []]
            for n in group:
                ret[min(1, n&bit)].append(n)
            return ret

        def find_max(zero, one, bit):
            if bit == 1:
                return (zero[0] ^ one[0]) if zero and one else 0
            if zero and one:
                zero_zero, zero_one = divide(zero, bit>>1)
                one_zero, one_one = divide(one, bit>>1)
                ret = 0
                if zero_zero and one_one:
                    ret = max(ret, find_max(zero_zero, one_one, bit>>1))
                if zero_one and one_zero:
                    ret = max(ret, find_max(zero_one, one_zero, bit>>1))
                if ret != 0:
                    return ret
                return max(ret,
                    find_max(zero_zero, one_zero, bit>>1),
                    find_max(zero_one, one_one, bit>>1))
            elif zero:
                zero_zero, zero_one = divide(zero, bit>>1)
                return find_max(zero_zero, zero_one, bit>>1)
            elif one:
                one_zero, one_one = divide(one, bit>>1)
                return find_max(one_zero, one_one, bit>>1)
            return 0

        nums = set(nums)
        m = max(nums)
        if not m:
            return 0
        bit = 2**int(math.log2(m))
        zero, one = divide(nums, bit)
        return find_max(zero, one, bit)


def bruteforce(nums):
    ret = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            ret = max(ret, nums[i]^nums[j])
    return ret


def gen(n):
    return [random.randint(0, (2**31)-1) for _ in range(n)]


@pytest.mark.parametrize('nums, expected', [
    ([3,10,5,25,2,8], 28),
    ([14,70,53,83,49,91,36,80,92,51,66,70], 127),
    ([0], 0),
    ([8,10,2], 10),
    ([4,6,7], 3),
    ([0b111000, 0b111000, 0b111000], 0),
    ([0b11110000, 0b00001110, 0b10101010, 0b01010101], 0b11111111),
    ([1363571383, 787643117, 1204541021, 1411690107, 1748407919], 2142505050),
    ([4, 5, 16], 21),
    (gen(100), None),
    (gen(100), None),
    (gen(100), None),
    (gen(100), None),
    ([37710,70350,99648,7015,65989,33902,48893,85155,49736,91159,5375,62001,33372,29226,51556,15147,75820,24624,36356,42353,57949,13978,19406,81813,14288,77475,78848,63955,98157,14610,25890,72574,29521,39004,97856,34806,67287,28486,86050,65045,65468,42440,46378,90088,70642,86668,13962,29947,5379,43894,71615,98157,3136,53758,31213,95011,10245,35928,47833,19704,73482,74069,56637,83442,22825,99042,74219,23952,40838,19438,5506,68319,17152,59754,72742,74444,96307,79816,72543,70036,40071,98662,98800,12407,20953,580,34577,51178,33028,98832,45804,22924,16428,47363,61681,3185,54087,71685,18902,62682,75496,85195,49967,91173,72136,40545,59109,75360,31411,3938,56662,88569,32877,80996,23338,55889,19199,42289,92685,68208,86178,56175,15469,71602,359,65,98482,30366,27520,29095,3541,28215,16398,59265,1598,28651,52488,16273,32606,46345,79877,9373,85925,38351,13095,13971,78977,64066,35844,86632,18645,68567,4946,75769,69137,2318,29870,65843,51955,73662,93033,71885,71130,95627,42095,723,86787,50004,57781,44414,94754,27721,84254,82782,27167,19930,98123,56185,49642,96907,1533,42158,81852,96420,41480,81810,9228,54436,46966,32252,30762,73909,67220,47036,96059,2362,4157,55557,75858,21957], 131059),
    ([0b1000], 0),
])
def test(nums, expected):
    expected = expected or bruteforce(nums)
    assert expected == Solution().findMaximumXOR(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
