#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

	The segment starts with 1.
	The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
	The segment:

		Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
		Continues the sequence in the same diagonal direction.
		Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.

Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

Example 1:

Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 5

Explanation:

The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:

Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 4

Explanation:

The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:

Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]

Output: 5

Explanation:

The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:

Input: grid = [[1]]

Output: 1

Explanation:

The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

Constraints:

	n == grid.length
	m == grid[i].length
	1 <= n, m <= 500
	grid[i][j] is either 0, 1 or 2.
"""
import json
from pathlib import Path
import enum
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        """When v shape starts only at the edges"""
        M, N = len(grid), len(grid[0])

        def get_next(i, j, di, dj):
            if di == 1:
                if i == M-1:
                    if dj == -1:
                        di = -1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            if di == -1:
                if i == 0:
                    if dj == 1:
                        di = 1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            if dj == 1:
                if j == N-1:
                    if di == 1:
                        dj = -1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            if dj == -1:
                if j == 0:
                    if di == -1:
                        dj = 1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            i, j = i+di, j+dj
            if 0<=i<M and 0<=j<N:
                return i, j, di, dj
            return None, None, di, dj


        def check(i, j, di, dj):
            ret = 0
            if grid[i][j] == 1:
                ret += 1
                while True:
                    i, j, di, dj = get_next(i, j, di, dj)
                    if i is None:
                        break
                    if grid[i][j] == (2 if ret%2 == 1 else 0):
                        ret += 1
                    else:
                        break
            return ret

        ret = 0
        for i in range(M):
            for j in range(N):
                for l in [
                    check(i, j, 1, -1),
                    check(i, j, 1, 1),
                    check(i, j, -1, 1),
                    check(i, j, -1, -1),
                ]:
                    ret = max(ret, l)
        return ret

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        """"""
        import sys
        sys.setrecursionlimit(100000)

        N, M = len(grid), len(grid[0])

        delta = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

        def new_length(cur: int, i: int, j: int) -> int:
            if cur == 0:
                return 0
            if grid[i][j] == [0, 2][cur%2]:
                return cur + 1
            return 0

        @lru_cache(None)
        def rec(i: int, j: int, d: int, v: bool) -> int:
            if not 0<=i<N or not 0<=j<M:
                return 0
            if grid[i][j] == 1:
                return 1

            di, dj = delta[d]
            ret = new_length(rec(i+di, j+dj, d, v), i, j)
            if v:
                nd = (d+1)%len(delta)
                ndi, ndj = delta[nd]
                ret = max(ret, new_length(rec(i+ndi, j+ndj, nd, False), i, j))
            return ret

        ret = 0
        for i in range(N):
            for j in range(M):
                for d in range(len(delta)):
                    ret = max(
                        ret,
                        rec(i, j, d, True),
                        rec(i, j, d, False)
                    )
        return ret

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        # ... new_length 함수는 동일 ...
        def new_length(cur: int, i: int, j: int) -> int:
            if cur == 0:
                return 0
            if grid[i][j] == [0, 2][cur%2]:
                return cur + 1
            return 0

        dp = [[[[0] * 2 for _ in range(4)] for _ in range(M)] for _ in range(N)]
        ret = 0

        # 올바른 시계 방향 순서의 delta 배열 사용
        # d=0:좌상, d=1:우상, d=2:우하, d=3:좌하 (에서 오는 경로)
        # 이 순서에 맞게 로직의 d 인덱스를 수정했습니다.
        delta = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        # --- 1단계: 모든 직선 경로(dp[][][][0])를 먼저 계산 ---
        # 순방향 i
        for i in range(N):
            for j in range(M): # 좌상에서 옴 (d=0)
                if grid[i][j] == 1: dp[i][j][0][0] = 1
                elif i > 0 and j > 0: dp[i][j][0][0] = new_length(dp[i-1][j-1][0][0], i, j)
            for j in range(M - 1, -1, -1): # 우상에서 옴 (d=1)
                if grid[i][j] == 1: dp[i][j][1][0] = 1
                elif i > 0 and j < M-1: dp[i][j][1][0] = new_length(dp[i-1][j+1][1][0], i, j)
        # 역방향 i
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1): # 우하에서 옴 (d=2)
                if grid[i][j] == 1: dp[i][j][2][0] = 1
                elif i < N-1 and j < M-1: dp[i][j][2][0] = new_length(dp[i+1][j+1][2][0], i, j)
            for j in range(M): # 좌하에서 옴 (d=3)
                if grid[i][j] == 1: dp[i][j][3][0] = 1
                elif i < N-1 and j > 0: dp[i][j][3][0] = new_length(dp[i+1][j-1][3][0], i, j)

        # --- 2단계: 계산된 직선 경로를 바탕으로 모든 V자 경로(dp[][][][1]) 계산 ---
        # 순방향 i
        for i in range(N):
            for j in range(M): # 좌상에서 옴 (d=0), 꺾이기 전 방향은 d=3(좌하)
                if i>0 and j>0:
                    prev_v = dp[i-1][j-1][0][1]
                    prev_s_turn = dp[i-1][j-1][3][0]
                    dp[i][j][0][1] = new_length(max(prev_v, prev_s_turn), i, j)
            for j in range(M-1, -1, -1): # 우상에서 옴 (d=1), 꺾이기 전 방향은 d=0(좌상)
                if i>0 and j<M-1:
                    prev_v = dp[i-1][j+1][1][1]
                    prev_s_turn = dp[i-1][j+1][0][0]
                    dp[i][j][1][1] = new_length(max(prev_v, prev_s_turn), i, j)
        # 역방향 i
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1): # 우하에서 옴 (d=2), 꺾이기 전 방향은 d=1(우상)
                if i<N-1 and j<M-1:
                    prev_v = dp[i+1][j+1][2][1]
                    prev_s_turn = dp[i+1][j+1][1][0]
                    dp[i][j][2][1] = new_length(max(prev_v, prev_s_turn), i, j)
            for j in range(M): # 좌하에서 옴 (d=3), 꺾이기 전 방향은 d=2(우하)
                if i<N-1 and j>0:
                    prev_v = dp[i+1][j-1][3][1]
                    prev_s_turn = dp[i+1][j-1][2][0]
                    dp[i][j][3][1] = new_length(max(prev_v, prev_s_turn), i, j)

        # DP 테이블 전체에서 최대값 찾기
        for i in range(N):
            for j in range(M):
                for d in range(4):
                    ret = max(ret, dp[i][j][d][0], dp[i][j][d][1])

        return ret


@pytest.mark.parametrize('args', [
    (([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]], 5)),
    (([[2,2,2,2,2],
       [2,0,2,2,0],
       [2,0,1,1,0],
       [1,0,2,2,2],
       [2,0,0,2,2]], 4)),
    (([[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]], 5)),
    (([[1]], 1)),
    (([[2,0,2,1,2,0,2,0,0,0,2],[2,1,1,0,2,0,2,0,2,2,1]], 3)),
    # ((json.load(open(Path(__file__).parent/'testcase.json')), 498)),
])
def test(args):
    assert args[-1] == Solution().lenOfVDiagonal(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
