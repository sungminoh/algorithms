#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.
"""

"""


def kmp(s, p):
    if not p:
        return [i for i in range(-1, len(s))]
    ret = []
    pi = get_pi(p)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j] :
            j = pi[j-1]
        if s[i] == p[j]:
            if j == len(p)-1:
                ret.append(i-len(p)+1)
                j = pi[j]
            else:
                j += 1
    return ret


def get_pi(p):
    j = 0
    pi = [0] * len(p)
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1;
            pi[i] = j;
    return pi


def kmp2(s, patterns):
    def build_lsp(p):
        ret = [0]
        i = 0
        for c in p[1:]:
            if c == p[i]:
                i += 1
                ret.append(i)
            else:
                while i > 0 and p[i] != c:
                    i = ret[i-1]
                if p[i] == c:
                    i += 1
                ret.append(i)
        return ret

    lsps = [build_lsp(p) for p in patterns]
    idxs = [0]*len(patterns)
    for c in s:
        for i in range(len(patterns)):
            if idxs[i] == len(patterns[i]):
                continue
            if patterns[i][idxs[i]] == c:
                idxs[i] += 1
            else:
                while idxs[i] > 0 and patterns[i][idxs[i]] != c:
                    idxs[i] = lsps[i][idxs[i]-1]
                if patterns[i][idxs[i]] == c:
                    idxs[i] += 1
    return [len(patterns[i]) == idxs[i] for i in range(len(patterns))]


