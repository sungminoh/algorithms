#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import operator


class BinaryIndexedTree:
    def __init__(self, size, key=None):
        self.tree = [None]*(size+1)
        self.key = key or operator.add

    def query(self, i):
        ret = 0
        i += 1
        while i > 0:
            if self.tree[i] is not None:
                ret = self.key(ret, self.tree[i])
            i -= i&-i
        return ret

    def update(self, i, v):
        i += 1
        while i < len(self.tree):
            self.tree[i] = self.key(self.tree[i], v)
            i += i&-i

