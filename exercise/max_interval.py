#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import pytest
import sys

def max_interval(arr, k):
    s = 0
    i, j = 0, 0
    ret = (i, j)
    m = 0
    while j < len(arr):
        s += arr[j]
        if j - i + 1 > k:
            if s / (j - i + 1) > m / (ret[1] - ret[0] + 1):
                m = s
                ret = (i, j)
            while arr[i] < s / (j - i + 1) and j - i + 1 > k:
                s -= arr[i]
                i += 1
                if s / (j - i + 1) > m / (ret[1] - ret[0] + 1):
                    m = s
                    ret = (i, j)
        else:
            m = s
            ret = (i, j)
        j += 1
    return ret


@pytest.mark.parametrize('arr, k, expected', [
    ([1,2,3,-100,99,-100,0], 2, (1,2)),
    ([1,2,3,100,99,-100,0], 2, (3,4)),
    ([1,2,3,100,0,100,0], 2, (3,5)),
    ([10,0,10,0,10,10,10,10], 2, (4,5)),
])
def test(arr, k, expected):
    assert expected == max_interval(arr, k)




if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
