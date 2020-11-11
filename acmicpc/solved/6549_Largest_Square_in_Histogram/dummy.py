#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
from random import randint


def main():
    n = int(sys.argv[1])
    h = int(sys.argv[2])
    print(n)
    for _ in range(n):
        print(randint(0, h))
    print(0)


if __name__ == '__main__':
    main()
