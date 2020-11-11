#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
# class Solution:
    # def numSquares(self, n: int) -> int:
        # def nsq(n, memo):
            # if n == 0:
                # return 0, 0
            # if n in memo:
                # return memo[n]
            # ret = float('inf')
            # min_used = float('inf')
            # for i in range(int(n**(1/2)), max(0, int((n//2)**(1/2))-1), -1):
                # n -= (i ** 2)
                # cnt, used = nsq(n, memo)
                # min_used = min(i, min_used, used)
                # ret = min(ret, 1 + cnt)
                # n += (i ** 2)
                # if i - 1 <= min_used:
                    # break
            # memo[n] = (ret, min_used)
            # return ret, min_used
        # return nsq(n, {})[0]


# class Solution:
    # def numSquares(self, n: int) -> int:
        # def nsq(n, cnt, ret, memo):
            # if n in memo:
                # return memo[n]
            # if cnt >= min(4, ret):
                # return cnt
            # if int(n ** (1/2)) ** 2 == n:
                # return 1 if n != 0 else 0
            # for i in range(int(n**(1/2)), 0, -1):
                # n -= (i ** 2)
                # ret = min(ret, 1 + nsq(n, cnt + 1, ret, memo))
                # n += (i ** 2)
            # memo[n] = ret
            # return ret
        # return nsq(n, 0, float('inf'), {})


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(int(n ** (1/2)), 0, -1)]
        ret = float('inf')
        memo = {}
        def nsq(n, i, cnt):
            nonlocal ret
            if n in memo:
                return memo[n]
            if cnt >= ret:
                return float('inf')
            if int(n ** (1/2)) ** 2 == n:
                return 1 if n != 0 else 0
            for j in range(i, len(squares)):
                m = n - squares[j]
                if m > 0:
                    ret = min(ret, 1 + nsq(m, j, cnt + 1))
            memo[n] = ret
            return ret
        return nsq(n, 0, 0)


def main():
    cases = [
        (12, 3),
        (13, 2),
        (25, 1),
        (144, 1),
        (31, 4),
        (0, 0),
        (1, 1),
        (16, 1),
        (88, 3),  # 36 36 16
        (7168, 4),
        (5156, 2),
        (192, 3),
        (240, 4),  # 100 100 36 4
        (6616, 3),  # 60^2, 54^2, 10^2
        (956, 4),
        (6024, 3),
        (2820, 3),
    ]
    for case, expected in cases:
        actual = Solution().numSquares(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
