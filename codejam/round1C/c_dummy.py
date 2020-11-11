#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from random import randrange
import sys


def main():
    n = int(sys.argv[1])
    print(1)
    ret = []
    for i in range(n):
        if i == 0:
            ret.append(randrange(1, 10**(min(i+2, 9))))
        else:
            ret.append(randrange(ret[i-1], 10**(min(i+2, 9))))
    print(n)
    print(' '.join(str(x) for x in ret))


if __name__ == '__main__':
    main()
